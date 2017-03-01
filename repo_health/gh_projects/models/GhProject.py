"""
GhProject.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

GitHub project model.
A Github project has two relationships to commits. A many to many and a foreign key.
Unsure the intention of the dual reltionship.
"""


from django.db import models as m


class GhProject(m.Model):
    
    url = m.CharField(max_length=255, blank=True, null=True)
    owner = m.ForeignKey('gh_users.GhUser', m.DO_NOTHING, blank=True, null=True)
    name = m.CharField(max_length=255)
    description = m.CharField(max_length=255, blank=True, null=True)
    language = m.CharField(max_length=255, blank=True, null=True)
    created_at = m.DateTimeField()
    ext_ref_id = m.CharField(max_length=24)
    forked_from = m.ForeignKey(
        'self', m.DO_NOTHING, db_column='forked_from', blank=True, null=True
    )
    deleted = m.IntegerField()

    # M2M fields added
    commits_m2m = m.ManyToManyField(
        'gh_commits.GhCommit', 
        through='gh_projects.GhProjectCommit',
    )

    maintainers = m.ManyToManyField(
        'gh_users.GhUser',
        through='gh_users.GhProjectMember',
        related_name='maintain_repos'
    )
    watchers = m.ManyToManyField(
        'gh_users.GhUser',
        through='gh_users.GhWatcher',
        related_name='watched_repos'
    )

    forks = m.ManyToManyField(
        'gh_projects.GhProject',
        through='gh_projects.GhFork',
        related_name='parents'
    )

    def __str__(self):
        return self.name

    def is_owned_by_org(self):
        return self.owner.is_org()

    class Meta:
        managed = False
        db_table = 'projects'
        unique_together = (('name', 'owner'),)
        verbose_name="GitHub Project"
