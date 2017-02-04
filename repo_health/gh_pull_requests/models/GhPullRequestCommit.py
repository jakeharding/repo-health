"""
GhPullRequestCommit.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
GitHub pull request commit.
"""


from django.db import models


class GhPullRequestCommit(models.Model):
    pull_request = models.ForeignKey('gh_pull_requests.GhPullRequest', models.DO_NOTHING)
    commit = models.ForeignKey('gh_commits.GhCommit', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pull_request_commits'
        unique_together = (('pull_request', 'commit'),)
