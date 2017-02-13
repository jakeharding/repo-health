"""tests.py - (C) Copyright - 2017

This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Test the generated models are functioning as expected.
Specifically test database relationships to show no error thrown and a result is returned.
"""


from django.test import TestCase
from .models import GhUser

class TestGhUser(TestCase):
    orgs_user = None
    watcher_user = None
    maintain_user = None
    

    def setUp(self):
        self.orgs_user = GhUser.objects.filter(
            organizations__isnull = False
        ).first()
        self.watcher_user = GhUser.objects.filter(
            watched_repos__isnull = False
        ).first()
        self.maintain_user = GhUser.objects.filter(
            maintain_repos__isnull = False
        ).first()
        
    
    def test_get_m2m(self):
        self.assertTrue(self.orgs_user.organizations.all())
        self.assertTrue(self.watcher_user.watched_repos.all())
        self.assertTrue(self.maintain_user.maintain_repos.all())      
        self.assertTrue(self.orgs_user.organizations.first().members.all())
        
