'''
GhIssue.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
 
 GitHub issue.
'''

from django.db import models


class GhIssue(models.Model):
    repo = models.ForeignKey('gh_projects.GhProject', models.DO_NOTHING, blank=True, null=True)
    reporter = models.ForeignKey(
        'gh_users.GhUser', models.DO_NOTHING, blank=True, null=True,
        related_name='reporter'
    )
    assignee = models.ForeignKey('gh_users.GhUser', models.DO_NOTHING, blank=True, null=True)
    issue_id = models.TextField()
    pull_request = models.IntegerField()
    pull_request_0 = models.ForeignKey(
        'gh_pull_requests.GhPullRequest', models.DO_NOTHING, db_column='pull_request_id', blank=True, null=True)  # Field renamed because of name conflict.
    created_at = models.DateTimeField()
    ext_ref_id = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'issues'
        verbose_name = 'GitHub Issue'