"""tests.py - (C) Copyright - 2017

This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Test the generated models are functioning as expected.
Specifically test database relationships to be sure an error is thrown and a result is returned.
"""


from django.test import TestCase
from .models import GhCommit, GhCommitComment

class TestGhCommit(TestCase):
    
    commit = None

    def setUp(self):
        self.commit = GhCommit.objects.filter(
            parents__isnull=False
        ).first()

    def test_get_commit(self):
        self.assertTrue(self.commit)
        self.assertTrue(self.commit.author)
        self.assertTrue(self.commit.committer)
    
    def test_get_commit_projects(self):
        self.assertTrue(self.commit.projects.all())

class TestGhCommitComment(TestCase):
    
    comment = None
    commment_user = None
    commit = None

    def setUp(self):
        self.comment = GhCommitComment.objects.first()
        self.user = self.comment.user
        self.commit = self.comment.commit

    def test_get_user_comments(self):
        #All the users comments.
        self.assertTrue(self.user.commit_comments.all())
        
        #all the commits the user has commented.
        self.assertTrue(self.user.comment_commits.all())

    def test_get_commit(self):
        #Comments for a commit
        self.assertTrue(self.commit.comments.all())
        #User who have commited on a comment
        self.assertTrue(self.commit.comment_users.all())
        

