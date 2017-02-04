"""
GhIssueLabel.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
GitHub issue label.
"""


from django.db import models


class GhIssueLabel(models.Model):
    label = models.ForeignKey('gh_projects.GhRepoLabel', models.DO_NOTHING)
    issue = models.ForeignKey('gh_issues.GhIssue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue_labels'
        unique_together = (('issue', 'label'),)
        
