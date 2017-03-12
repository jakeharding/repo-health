"""
serializers.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializer for issue stats of a GitHub repo.
"""


from rest_framework import serializers as s


class GhIssueStatsSerializer(s.Serializer):

    issues_count = s.SerializerMethodField()
    # issues_last_year = s.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repo = args[0]

    def get_issues_count(self, repo):
        return repo.issues_count
