"""
GhIssue.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
 
 GitHub issue. 
"""

from django.db import models


class GhIssue(models.Model):
    repo = models.ForeignKey('gh_projects.GhProject', models.DO_NOTHING,
                             blank=True, null=True,
                             related_name='issues'
                             )

    reporter = models.ForeignKey(
        'gh_users.GhUser', models.DO_NOTHING, blank=True, null=True,
        related_name='reporter'
    )
    assignee = models.ForeignKey('gh_users.GhUser', models.DO_NOTHING,
        blank=True, null=True, related_name='assigned_issues')
    issue_id = models.TextField()
    pull_request = models.IntegerField()

    # Field renamed because of name conflict
    pull_request_0 = models.ForeignKey(
        'gh_pull_requests.GhPullRequest', 
        models.DO_NOTHING, 
        db_column='pull_request_id', 
        blank=True, null=True
    )
    created_at = models.DateTimeField()
    ext_ref_id = models.CharField(max_length=24)

    # M2M fields add
    comment_users = models.ManyToManyField(
        'gh_users.GhUser', 
        through='gh_issues.GhIssueComment',
        related_name='comment_issues'
    )

    labels = models.ManyToManyField(
        'gh_projects.GhRepoLabel',
        through='gh_issues.GhIssueLabel', related_name='label_issues'
    )

    def __str__(self):
        return "Issue for: %s" % self.repo.name

    class Meta:
        db_table = 'issues'
        verbose_name = 'GitHub Issue'
