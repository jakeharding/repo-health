"""
GhPullRequest.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
 
 GitHub pull request.
"""



from django.db import models


class GhPullRequest(models.Model):
    head_repo = models.ForeignKey(
        'gh_projects.GhProject', models.DO_NOTHING, blank=True, null=True,
        related_name='prs_from'
    )
    base_repo = models.ForeignKey(
        'gh_projects.GhProject', models.DO_NOTHING,
        related_name='prs_to',        
    )
    head_commit = models.ForeignKey(
        'gh_commits.GhCommit', models.DO_NOTHING, blank=True, null=True,
        related_name="commit_from"
    )
    base_commit = models.ForeignKey('gh_commits.GhCommit', models.DO_NOTHING,
        related_name="commit_to"        
    )
    user = models.ForeignKey('gh_users.GhUser', models.DO_NOTHING)
    pullreq_id = models.IntegerField()
    intra_branch = models.IntegerField()
    merged = models.IntegerField()

    #Added M2M
    commits = models.ManyToManyField('gh_commits.GhCommit',
        through = 'gh_pull_requests.GhPullRequestCommit'
    )

    def __str__(self):
        return "PR base project: %s" % self.base_repo.name

    @property
    def created_at(self):
        """Convenience method to determine when pull request was created.
        For now use the head commit's created_at field.
        """
        return self.head_commit.created_at

    class Meta:
        managed = False
        db_table = 'pull_requests'
        unique_together = (('pullreq_id', 'base_repo'),)
        verbose_name = 'GitHub Pull Request'
