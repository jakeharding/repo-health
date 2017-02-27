"""
GhPullRequestComment.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
GitHub pull request comment.
"""

from django.db import models


class GhPullRequestComment(models.Model):
    pull_request = models.ForeignKey(
        'gh_pull_requests.GhPullRequest', models.DO_NOTHING,
        related_name='comments'
    )
    user = models.ForeignKey('gh_users.GhUser', models.DO_NOTHING)
    comment_id = models.TextField()
    position = models.IntegerField(blank=True, null=True)
    body = models.CharField(max_length=256, blank=True, null=True)
    commit = models.ForeignKey('gh_commits.GhCommit', models.DO_NOTHING)
    created_at = models.DateTimeField()
    ext_ref_id = models.CharField(max_length=24, primary_key=True)

    def __str__(self):
        return "PR comment by: %s For base repo: %s" %(self.user.login, self.pull_request.base_repo)

    class Meta:
        managed = False
        db_table = 'pull_request_comments'
        verbose_name = 'GitHub Pull Request Comment'
