"""
serializers.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializer for issue stats of a GitHub repo.
"""

import calendar
import datetime
from rest_framework import serializers as s
from ..models import GhIssueEvent


class GhIssueStatsSerializer(s.Serializer):

    _issues_last_year = None

    issues_count = s.SerializerMethodField()
    issues_closed_last_year = s.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        repo = args[0]
        one_yr_from_most_recent = repo.most_recent_issue_created - datetime.timedelta(days=366)
        self._issues_last_year = repo.issues.filter(created_at__gte=one_yr_from_most_recent)

    def get_issues_count(self, repo):
        return repo.issues_count

    def get_issues_closed_last_year(self, repo):
        closed = self._issues_last_year.filter(
            events__action=GhIssueEvent.CLOSED_ACTION
        ).order_by('-events__created_at').distinct()
        opened_count_for_year = []
        if closed.exists():
            # Some projects don't have issues in Github
            dt_to_filter = closed.last().created_at
            for mon in range(12):
                days_in_mon = calendar.monthrange(dt_to_filter.year, dt_to_filter.month)[1]
                opened_count_for_year.append(closed.filter(
                    events__created_at__year=dt_to_filter.year,
                    events__created_at__month=dt_to_filter.month).count())
                dt_to_filter += datetime.timedelta(days=days_in_mon)
        else:
            opened_count_for_year = [0] * 12
        return opened_count_for_year
