"""
GhCommitComment.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

GitHub commit comment.
"""


from django.db import models


class GhCommitComment(models.Model):
    commit = models.ForeignKey('gh_commits.GhCommit', models.DO_NOTHING)
    user = models.ForeignKey('gh_users.GhUser', models.DO_NOTHING)
    body = models.CharField(max_length=256, blank=True, null=True)
    line = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    comment_id = models.IntegerField(unique=True)
    ext_ref_id = models.CharField(max_length=24)
    created_at = models.DateTimeField()

    def __str__(self):
        return "User: %s" % self.user.login

    class Meta:
        managed = False
        db_table = 'commit_comments'
        verbose_name='GitHub Commit Comment'
