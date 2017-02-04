"""
GhRepoMilestone.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

GitHub repo milestones model.
"""

from django.db import models

class GhRepoMilestone(models.Model):
    repo = models.ForeignKey('gh_projects.GhProject', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=24)
    ext_ref_id = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'repo_milestones'
        verbose_name = 'GitHub Repo Milestone'
