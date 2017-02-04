"""
GhIssueEvent.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
GitHub issue event.
"""

from django.db import models


class GhIssueEvent(models.Model):
    event_id = models.TextField()
    issue = models.ForeignKey('gh_issues.GhIssue', models.DO_NOTHING)
    actor = models.ForeignKey('gh_users.GhUser', models.DO_NOTHING)
    action = models.CharField(max_length=255)
    action_specific = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    ext_ref_id = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'issue_events'
        verbose_name = 'GitHub Issue Event'
        
