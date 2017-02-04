'''
GhCommitParent.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

GitHub commit parent model.
'''

from django.db import models


class GhCommitParent(models.Model):
    commit = models.ForeignKey(
        'gh_commits.GhCommit', models.DO_NOTHING
    )
    parent = models.ForeignKey(
        'gh_commits.GhCommit', models.DO_NOTHING,
        related_name="parent"        
    )

    class Meta:
        managed = False
        db_table = 'commit_parents'
        unique_together = (('commit', 'parent'),)