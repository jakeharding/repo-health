"""
GhIssueStatsSerializer.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializer for issue stats of a GitHub repo.
"""

import datetime
from rest_framework import serializers as s
from ..models import GhIssueEvent, GhIssueComment
from .TotalAndOpenIssueLabelSerial import TotalAndOpenIssueLabelSerial
from repo_health.gh_projects.models import GhRepoLabel
from repo_health.index.mixins import CountForPastYearMixin
from repo_health.metrics.serializers import MetricField, ChartField


class GhIssueStatsSerializer(s.Serializer, CountForPastYearMixin):

    # Chart names
    ISSUES_CLOSED = 'issues_closed'
    ISSUES_OPENED = 'issues_opened'

    card_title = s.SerializerMethodField()
    issues_count = s.SerializerMethodField()
    issues_closed_last_year = s.SerializerMethodField()
    issues_opened_last_year = s.SerializerMethodField()
    merged_count = s.SerializerMethodField()
    avg_lifetime = s.SerializerMethodField()
    # popular_labels = s.SerializerMethodField()
    avg_maintainer_comments_per_issue = s.SerializerMethodField()
    most_recent_created_at = s.SerializerMethodField()
    _charts = None

    @property
    def charts(self):
        return self._charts

    @charts.setter
    def charts(self, charts):
        self._charts = charts

    def __init__(self, *args, **kwargs):
        """
        Reset _charts to empty array for every object initialized.
        :param args: 
        :param kwargs: 
        """
        super().__init__(*args, **kwargs)
        self.charts = []

    def get_card_title(self, repo):
        return MetricField(True, None, 0, None, "Issues")

    def get_issues_count(self, repo):
        return MetricField(True, "Number of issues", 1, None, repo.issues_count)

    def get_issues_closed_last_year(self, repo):
        metric, most_recent = self.get_count_list_for_year(repo.issues.filter(events__action=GhIssueEvent.CLOSED_ACTION).distinct())
        self._charts.append(ChartField(self.ISSUES_CLOSED, most_recent, "Closed issues last year", None, None, 1))
        return MetricField(True, "Closed issues last year", 2, self.ISSUES_CLOSED, metric)

    def get_issues_opened_last_year(self, repo):
        metric, most_recent = self.get_count_list_for_year(repo.issues)
        self._charts.append(ChartField(self.ISSUES_OPENED, most_recent, "Open issues last year", None, None, 1))
        return MetricField(True, "Open issues last year", 3, self.ISSUES_OPENED, metric)

    def get_most_recent_created_at(self, repo):
        most_recent = repo.issues.order_by('-created_at').first().created_at
        return MetricField(True, 'Most recent issue created at', 4, None, most_recent, True)

    def get_merged_count(self, repo):
        merged_count = repo.issues.filter(events__action=GhIssueEvent.MERGED_ACTION).count()
        return MetricField(True, "Merged issues", 5, None, merged_count)

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
        return MetricField(True, "Average issue lifetime", 6, None, avg)

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
        avg_coms = round(comments_from_m / repo.issues.count(), 5)
        return MetricField(True, 'Average maintainer comments per issue', 6, None, avg_coms)