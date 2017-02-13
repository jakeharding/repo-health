"""
GhRepoLabel.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

GitHub repo Labels model.
"""

from django.db import models

class GhRepoLabel(models.Model):
    repo = models.ForeignKey(
      'gh_projects.GhProject', models.DO_NOTHING, blank=True, null=True
    )
    name = models.CharField(max_length=24)
    ext_ref_id = models.CharField(max_length=24)

    #Add m2m
    issues = models.ManyToManyField(
        'gh_issues.GhIssue',
        through='gh_issues.GhIssueLabel'
    )

    def __str__(self):
        return "Label name: '%s' for repo: %s" % (self.name, self.repo.name)

    class Meta:
        managed = False
        db_table = 'repo_labels'
        verbose_name = 'GitHub Repo Label'
