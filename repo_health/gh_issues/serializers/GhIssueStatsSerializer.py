"""
serializers.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializer for issue stats of a GitHub repo.
"""

from rest_framework import serializers as s
from ..models import GhIssueEvent
from repo_health.index.mixins import CountForPastYearMixin


class GhIssueStatsSerializer(s.Serializer, CountForPastYearMixin):

    _label_names = None

    issues_count = s.SerializerMethodField()
    issues_closed_last_year = s.SerializerMethodField()
    issues_opened_last_year = s.SerializerMethodField()
    merged_count = s.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        repo = args[0]
        self._label_names = repo.labels.values_list('name', flat=True)

    def get_issues_count(self, repo):
        return repo.issues_count

    def get_issues_closed_last_year(self, repo):
        return self.get_count_list_for_year(repo.issues.filter(events__action=GhIssueEvent.CLOSED_ACTION).distinct())

    def get_issues_opened_last_year(self, repo):
        return self.get_count_list_for_year(repo.issues)
