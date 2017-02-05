"""tests.py - (C) Copyright - 2017

This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Test the generated models are functioning as expected.
Specifically test database relationships to be sure an error is thrown and a result is returned.
"""


from django.test import TestCase
from .models import GhIssue, GhIssueComment

class TestGhIssue(TestCase):
    issue = None
    issue_user = None

    def setUp(self):
        self.issue = GhIssue.objects.filter(
            comments__isnull=False
        ).first()
        self.issue_user = self.issue.comment_users.first()
    
    def test_m2m(self):
        self.assertTrue(self.issue_user.comment_issues.all())
        self.assertTrue(self.issue.comment_users.all())
