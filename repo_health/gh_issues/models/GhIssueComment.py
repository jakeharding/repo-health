"""
GhIssueComment.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
 
 GitHub issue comment.
"""


from django.db import models


class GhIssueComment(models.Model):
    issue = models.ForeignKey('gh_issues.GhIssue', models.DO_NOTHING, related_name='comments')
    user = models.ForeignKey('gh_users.GhUser', models.DO_NOTHING, related_name='issue_comments')
    comment_id = models.TextField()
    created_at = models.DateTimeField()
    ext_ref_id = models.CharField(max_length=24)

    def __str__(self):
        return "Comment by: %s" % self.user.login

    class Meta:
        managed = False
        db_table = 'issue_comments'
        verbose_name = 'GitHub Issue Comment'
