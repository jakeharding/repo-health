"""
GhCommit.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

GitHub commit model.
"""


from django.db import models


class GhCommit(models.Model):
    sha = models.CharField(unique=True, max_length=40, blank=True, null=True)
    author = models.ForeignKey(
        'gh_users.GhUser', models.DO_NOTHING, 
        blank=True, null=True, related_name='author'
    )
    committer = models.ForeignKey(
        'gh_users.GhUser', models.DO_NOTHING, 
        blank=True, null=True, related_name="committer"
    )
    project = models.ForeignKey(
        'gh_projects.GhProject', models.DO_NOTHING, blank=True, null=True,
        related_name="commits_fk"
    )
    created_at = models.DateTimeField()
    ext_ref_id = models.CharField(max_length=24)

    #Added fields for many to many relationships
    comment_users = models.ManyToManyField(
        "gh_users.GhUser", 
        through="gh_commits.GhCommitComment"
    )
    projects = models.ManyToManyField(
        'gh_projects.GhProject', 
        through='gh_projects.GhProjectCommit'
    )
    parents = models.ManyToManyFields(
        'gh_commits.GhCommit',
        through='gh_commits.GhCommitParent'
    )

    def __str__(self):
        return "Project: %s Author: %s" %(self.project.name, self.author.login)

    class Meta:
        managed = False
        db_table = 'commits'
        verbose_name="GitHub Commit"
