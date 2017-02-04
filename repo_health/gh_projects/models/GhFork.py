'''
GhFork.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
GitHub fork model.
'''


from django.db import models


class GhFork(models.Model):
    forked_project = models.ForeignKey(
      'gh_projects.GhProject', models.DO_NOTHING,
      related_name="forked_project"
    )
    forked_from = models.ForeignKey(
      'gh_projects.GhProject', models.DO_NOTHING,
    )
    fork_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField()
    ext_ref_id = models.CharField(max_length=24)

    def __str__(self):
          return self.forked_project.name

    class Meta:
        managed = False
        db_table = 'forks'
        unique_together = (('forked_project', 'forked_from'),)
        verbose_name = 'GitHub Fork'