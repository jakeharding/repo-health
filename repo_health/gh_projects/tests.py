"""tests.py - (C) Copyright - 2017

This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Test projects
"""


import datetime
from django.test import TestCase, Client
from django.db import models as m
from rest_framework import status
from rest_framework.test import APITestCase
from .models import GhProject, GhRepoLabel


class TestGhProject(TestCase):
    """
    Test the generated models are functioning as expected.
    Specifically test database relationships to show no error thrown and a result is returned.
    """

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
    """
    Test the REST api to retrieve a project.
    """

    project = None

    def setUp(self):
        self.project = GhProject.objects.last()
        self.project_no_prs = GhProject.objects.annotate(prs_to_count=m.Count('prs_to')).order_by('prs_to_count').first()
        # Django has a lot of pull requests
        self.django = GhProject.objects.get(name='django', owner__login='django')

    def test_api_get_project(self):
        r = self.client.get('/api/v1/gh-projects', {'owner__login':self.project.owner.login, 'name':self.project.name})
        self.assertTrue(status.is_success(r.status_code))
        import pprint as pp; pp.pprint(r.data)
        self.assertEqual(r.data['name'], self.project.name)
        self.assertEqual(r.data['id'], self.project.id)

    def test_api_get_project_not_found(self):
        # Test with a bad owner login
        r_with_bad_owner = self.client.get('/api/v1/gh-projects', {'owner__login':'incoherehnet giibbuusrish', 'name':self.project.name})
        self.assertTrue(status.is_client_error(r_with_bad_owner.status_code))

        # Test with a bad repo name
        r_with_bad_repo = self.client.get('/api/v1/gh-projects', {
            'owner__login': self.project.owner.login, 'name': 'gibiberishsh'
        })
        self.assertTrue(status.is_client_error(r_with_bad_repo.status_code))

        # Test with a bad param
        r_with_bad_key = self.client.get('/api/v1/gh-projects', {
            'giibbier': self.project.owner.login, 'name': self.project.name
        })
        self.assertTrue(status.is_client_error(r_with_bad_key.status_code))

        # test with no param
        r_with_no_param = self.client.get('/api/v1/gh-projects')
        self.assertTrue(status.is_client_error(r_with_no_param.status_code))

    def test_get_pr_stats(self):
        r = self.client.get('/api/v1/gh-projects/%d/pull-requests' % self.django.id)
        self.assertTrue(status.is_success(r.status_code), 'Status code was: %d' % r.status_code)
        # Check for a few custom fields of the serialozer
        self.assertTrue(r.data['pr_count'] and isinstance(r.data['pr_count'], int))
        self.assertTrue(r.data['prs_last_year'] and isinstance(r.data['prs_last_year'], list))
        self.assertTrue(
            r.data.get('latest_pr_created_at') and isinstance(r.data['latest_pr_created_at'], datetime.datetime)
        )
        self.assertTrue(r.data['contrib_most_prs'] and isinstance(r.data['contrib_most_prs'], str))
        self.assertTrue(
            r.data.get('prs_no_maintainer_comments') and isinstance(r.data['prs_no_maintainer_comments'], int))


        # Test a repo with no prs to be sure no errors are thrown
        self.client.get('/api/v1/gh-projects/%d/pull-requests' % self.project_no_prs.id)



