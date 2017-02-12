"""tests.py - (C) Copyright - 2017

This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Test the generated models are functioning as expected.
Specifically test database relationships to show no error thrown and a result is returned.
"""


from django.urls import reverse
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from .models import GhProject, GhRepoLabel


class TestGhProject(TestCase):
    project = None
    client = None 

    def setUp(self):
        self.project = GhProject.objects.filter(
            forked_from__isnull=False,
            commits_fk__isnull=False,
        ).first()
        self.client = Client()


    def test_get_project(self):
        self.assertTrue(self.project)

    def test_get_projects_commits(self):
        commits_fk = self.project.commits_fk.all()
        commits_m2m = self.project.commits_m2m.all()
        self.assertTrue(commits_fk)
        self.assertTrue(commits_m2m)

    def test_get_forked_from(self):
        self.assertTrue(self.project.forked_from)

    def test_get_repo_labels(self):
        labels = GhRepoLabel.objects.filter(repo__isnull=False)
        self.assertTrue(labels)


class GhProjectApiTest(APITestCase):

    project = None
    def setUp(self):
        self.project = GhProject.objects.last()

    def test_api_get_project(self):
        r = self.client.get('/api/v1/gh-projects', {'owner__login':self.project.owner.login, 'name':self.project.name})
        self.assertTrue(status.is_success(r.status_code))
        self.assertEqual(r.data['name'], self.project.name)
        self.assertEqual(r.data['id'], self.project.id)
        
        