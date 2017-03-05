"""
serializers.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializers for pull requests.
"""

import datetime
import calendar
from django.db import models as m
from rest_framework import serializers as s
from repo_health.gh_users.models import GhUser
from ..models import GhPullRequestHistory, GhPullRequest


class GhPullRequestStatsSerializer(s.Serializer):
    _most_recent_history = None
    _opened_histories = None
    _contrib_most_prs = None
    _maintainers = None
    _maintainers_count = None

    pr_count = s.SerializerMethodField()
    prs_last_year = s.SerializerMethodField()
    latest_pr_created_at = s.SerializerMethodField()
    contrib_most_prs = s.SerializerMethodField()
    prs_no_maintainer_comments = s.SerializerMethodField()
    maintainers_count = s.SerializerMethodField()
    prs_no_comments = s.SerializerMethodField()
    avg_lifetime = s.SerializerMethodField()
    not_maintainer_prs = s.SerializerMethodField()
    avg_comment_per_pr = s.SerializerMethodField()
    prs_from_outside_org = s.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        repo = args[0]
        self._opened_histories = GhPullRequestHistory.objects.filter(
            pull_request__base_repo=repo,
            action=GhPullRequestHistory.OPENED_ACTION,
        ).order_by('-created_at')

        self._most_recent_history = self._opened_histories.first()

        # Get user with the most pull requests for this repo
        self._contrib_most_prs = GhUser.objects.filter(
            pull_requests__base_repo=repo,
        ).annotate(
            contrib_prs=m.Count('pull_requests')
        ).order_by('-contrib_prs').first()

        self._maintainers = repo.maintainers.all()

    def get_pr_count(self, repo):
        return repo.pr_count

    def get_prs_last_year(self, repo):
        one_year = datetime.timedelta(days=366)
        opened_count_for_year = []

        if self._most_recent_history:
            opened_prev_year = self._opened_histories.filter(created_at__gte=self._most_recent_history.created_at - one_year)
            dt_to_filter = opened_prev_year.last().created_at

            for m in range(12):
                days_in_mon = calendar.monthrange(dt_to_filter.year, dt_to_filter.month)[1]
                opened_count_for_year.append(opened_prev_year.filter(
                    created_at__year=dt_to_filter.year,
                    created_at__month=dt_to_filter.month).count())
                dt_to_filter += datetime.timedelta(days=days_in_mon)
        return opened_count_for_year

    def get_latest_pr_created_at(self, repo):
        return self._most_recent_history.created_at if self._most_recent_history else None

    def get_contrib_most_prs(self, repo):
        return self._contrib_most_prs.login if self._contrib_most_prs else None

    def get_prs_no_maintainer_comments(self, repo):
        return repo.prs_to.exclude(comment_users__in=self._maintainers).count()

    def get_maintainers_count(self, repo):
        return self._maintainers.count()

    def get_prs_no_comments(self, repo):
        return repo.prs_to.annotate(comments_count=m.Count('comments')).filter(comments_count=0).count()

    def get_avg_lifetime(self, repo):
        avg = closed = 0
        # An inefficient way to calculate average but I haven't got the aggregation to work
        if repo.pr_count > 0:  # prevent divide by zero
            td = datetime.timedelta()
            for p in repo.prs_to.all():
                if p.closed_at:
                    closed += 1
                    td += p.closed_at - p.created_at
            avg = (td / closed).days

        # Save this code to hopefully aggregate the average at the database level sometime.
        agg = GhPullRequest.objects.raw(
            "SELECT `pull_requests`.`id`, `pull_request_history`.`created_at` as `created_at`, `t`.`created_at` as " +
            "`closed_at` from `pull_requests` join `pull_request_history` on `pull_request_history`." +
            "`pull_request_id` = `pull_requests`.`id` join `pull_request_history` `t` on`pull_request_history`." +
            "`pull_request_id` = `pull_requests`.`id` where `t`.`action` = 'closed' and `pull_request_history`." +
            "`action` = 'opened' and `pull_requests`.`base_repo_id` = %s", [repo.id],

        )
        # agg = repo.prs_to \
        #     .annotate(closed_at=m.Case(
        #         m.When(
        #             history__action=GhPullRequestHistory.CLOSED_ACTION,
        #             then=m.F('history__created_at'),
        #         ), output_field=m.DateTimeField(),
        #     )) \
        #     .annotate(created_at=m.Case(
        #         m.When(
        #             history__action=GhPullRequestHistory.OPENED_ACTION,
        #             then=m.F('history__created_at'),
        #         ), output_field=m.DateTimeField(),
        #     )) \
        #     .values('created_at', 'closed_at', 'id', 'history__action') \
        #     .exclude(m.Q(history__action=GhPullRequestHistory.CLOSED_ACTION) & m.Q(closed_at__isnull=True)).query
            # .aggregate(avg=m.Avg(m.F('created_at') - m.F('closed_at'), output_field=m.DurationField()))
        print(agg)

        return avg

    def get_not_maintainer_prs(self, repo):
        return repo.prs_to.exclude(user__in=self._maintainers).count()

    def get_avg_comment_per_pr(self, repo):
        avg_agg = repo.prs_to.annotate(comment_count=m.Count('comments')) \
            .aggregate(avg=m.Avg('comment_count'))
        return avg_agg['avg']

    def get_prs_from_outside_org(self, repo):
        if repo.is_owned_by_org():
            return repo.prs_to.exclude(user__organizations=repo.owner).count()

    class Meta:
        model = 'gh_projects.GhProject'
        fields = ('pr_count', )

