"""
tests.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Test the generated models are functioning as expected.
"""


from django.test import TestCase
from factory.django import DjangoModelFactory

from .models import GhProject

class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = GhProject

class TestGhProject(TestCase):
    
    # def setUp(self):
    #     """Setup ran before every test."""
    #     pass

    def test_get_project(self):
        project = GhProject.objects.get(id=1)
        self.assertEqual(None, project)        
