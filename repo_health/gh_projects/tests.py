"""tests.py - (C) Copyright - 2017

This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Test the generated models are functioning as expected.
Specifically test database relationships to show no error thrown and a result is returned.
"""


from django.test import TestCase
from .models import GhProject


class TestGhProject(TestCase):


    def setUp(self):
        self.project = GhProject.objects.filter(
            forked_from__isnull=False,
            commits_fk__isnull=False,
        ).first()



    def test_get_project(self):
        self.assertTrue(self.project)

    def test_get_projects_commits(self):
        commits_fk = self.project.commits_fk.all()
        commits_m2m = self.project.commits_m2m.all()
        self.assertTrue(commits_fk)
        self.assertTrue(commits_m2m)

    def test_get_forked_from(self):
        self.assertTrue(self.project.forked_from)
        