"""
GhProjectCommit.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

GitHub project commit model.
"""

from django.db import models as m

class GhProjectCommit(m.Model):
    project = m.ForeignKey('gh_projects.GhProject', m.DO_NOTHING)
    commit = m.ForeignKey('gh_commits.GhCommit', m.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_commits'
        unique_together = (('project', 'commit'),)
