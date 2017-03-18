"""
serializers.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializer for issue stats of a GitHub repo.
"""

import datetime
from django.db import models as m
from rest_framework import serializers as s
from ..models import GhIssueEvent, GhIssueComment
from .TotalAndOpenIssueLabelSerial import TotalAndOpenIssueLabelSerial
from repo_health.gh_projects.models import GhRepoLabel
from repo_health.index.mixins import CountForPastYearMixin


class GhIssueStatsSerializer(s.Serializer, CountForPastYearMixin):

    _label_names = None

    issues_count = s.SerializerMethodField()
    issues_closed_last_year = s.SerializerMethodField()
    issues_opened_last_year = s.SerializerMethodField()
    merged_count = s.SerializerMethodField()
    avg_lifetime = s.SerializerMethodField()
    popular_labels = s.SerializerMethodField()
    avg_maintainer_comments_per_issue = s.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        repo = args[0]

    def get_issues_count(self, repo):
        return repo.issues_count

    def get_issues_closed_last_year(self, repo):
        return self.get_count_list_for_year(repo.issues.filter(events__action=GhIssueEvent.CLOSED_ACTION).distinct())

    def get_issues_opened_last_year(self, repo):
        return self.get_count_list_for_year(repo.issues)

    def get_merged_count(self, repo):
        return repo.issues.filter(events__action=GhIssueEvent.MERGED_ACTION).count()

    def get_avg_lifetime(self, repo):
        # Similar inefficiency as the PR stats but must access the fields a little differently.
        avg = closed = 0
        if repo.issues_count is not 0:
            td = datetime.timedelta()
            closed_issues = repo.issues.prefetch_related('events').filter(events__action=GhIssueEvent.CLOSED_ACTION,
                                                                          created_at__isnull=False)

            for i in closed_issues.all():
                closed += 1
                close_event = i.events.filter(action=GhIssueEvent.CLOSED_ACTION).order_by('-created_at').first()
                if not isinstance(i.created_at, type(None)):
                    td += (close_event.created_at - i.created_at)
            avg = (td / closed).days if closed > 0 else closed
        return avg

    def get_popular_labels(self, repo):
        # Raw SQL.
        labels_by_count_for_repo = GhRepoLabel.objects.raw(
            'SELECT t.*, count(t.id) as repos_labels FROM repo_labels t join issue_labels il on il.label_id=t.id\
            where t.repo_id = %d GROUP BY t.id ORDER BY repos_labels desc;' % repo.id)

        top_five = labels_by_count_for_repo[:5]
        response_data = []
        for l in top_five:
            label_serial = TotalAndOpenIssueLabelSerial(l)
            response_data.append(label_serial.data)
        return response_data

    def get_avg_maintainer_comments_per_issue(self, repo):
        comments_from_m = GhIssueComment.objects.filter(
            issue__in=repo.issues.all(),
            user__in=repo.maintainers.all()
        ).count()
        return comments_from_m / repo.issues.count()