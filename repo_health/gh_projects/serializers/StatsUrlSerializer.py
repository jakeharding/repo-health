"""
StatsUrlSerializer.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializer for urls to retrieve stats about a GitHub repo.
"""

from rest_framework.serializers import Serializer, SerializerMethodField
from rest_framework.reverse import reverse

class StatsUrlsSerializer(Serializer):

    repo_details_url = SerializerMethodField()
    issue_stats_url = SerializerMethodField()
    pr_stats_url = SerializerMethodField()

    def get_repo_details_url(self, repo):
        return self.get_stats_url('gh-project-detail', repo.id)

    def get_issue_stats_url(self, repo):
        return self.get_stats_url('gh-project-issues', repo.id)

    def get_pr_stats_url(self, repo):
        return self.get_stats_url('gh-project-pull-requests', repo.id)

    def get_stats_url(self, url_name, repo_id):
        return reverse(url_name, args=[repo_id], request=self.context.get('request'))