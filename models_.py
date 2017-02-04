# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models





# class CommitComments(models.Model):
#     commit = models.ForeignKey('Commits', models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     body = models.CharField(max_length=256, blank=True, null=True)
#     line = models.IntegerField(blank=True, null=True)
#     position = models.IntegerField(blank=True, null=True)
#     comment_id = models.IntegerField(unique=True)
#     ext_ref_id = models.CharField(max_length=24)
#     created_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'commit_comments'


# class CommitParents(models.Model):
#     commit = models.ForeignKey('Commits', models.DO_NOTHING)
#     parent = models.ForeignKey('Commits', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'commit_parents'
#         unique_together = (('commit', 'parent'),)


# class Commits(models.Model):
#     sha = models.CharField(unique=True, max_length=40, blank=True, null=True)
#     author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     committer = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'commits'


# class Followers(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     follower = models.ForeignKey('Users', models.DO_NOTHING)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'followers'
#         unique_together = (('user', 'follower'),)


# class Forks(models.Model):
#     forked_project = models.ForeignKey('Projects', models.DO_NOTHING)
#     forked_from = models.ForeignKey('Projects', models.DO_NOTHING)
#     fork_id = models.IntegerField(unique=True)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'forks'
#         unique_together = (('forked_project', 'forked_from'),)


# class IssueComments(models.Model):
#     issue = models.ForeignKey('Issues', models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     comment_id = models.TextField()
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'issue_comments'


# class IssueEvents(models.Model):
#     event_id = models.TextField()
#     issue = models.ForeignKey('Issues', models.DO_NOTHING)
#     actor = models.ForeignKey('Users', models.DO_NOTHING)
#     action = models.CharField(max_length=255)
#     action_specific = models.CharField(max_length=50, blank=True, null=True)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'issue_events'


# class IssueLabels(models.Model):
#     label = models.ForeignKey('RepoLabels', models.DO_NOTHING)
#     issue = models.ForeignKey('Issues', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'issue_labels'
#         unique_together = (('issue', 'label'),)


# class Issues(models.Model):
#     repo = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
#     reporter = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     assignee = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     issue_id = models.TextField()
#     pull_request = models.IntegerField()
#     pull_request_0 = models.ForeignKey('PullRequests', models.DO_NOTHING, db_column='pull_request_id', blank=True, null=True)  # Field renamed because of name conflict.
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'issues'


# class OrganizationMembers(models.Model):
#     org = models.ForeignKey('Users', models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     created_at = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'organization_members'
#         unique_together = (('org', 'user'),)


# class ProjectCommits(models.Model):
#     project = models.ForeignKey('Projects', models.DO_NOTHING)
#     commit = models.ForeignKey(Commits, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'project_commits'
#         unique_together = (('project', 'commit'),)


# class ProjectMembers(models.Model):
#     repo = models.ForeignKey('Projects', models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'project_members'
#         unique_together = (('repo', 'user'),)


# class Projects(models.Model):
#     url = models.CharField(max_length=255, blank=True, null=True)
#     owner = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     language = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)
#     forked_from = models.ForeignKey('self', models.DO_NOTHING, db_column='forked_from', blank=True, null=True)
#     deleted = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'projects'
#         unique_together = (('name', 'owner'),)


# class PullRequestComments(models.Model):
#     pull_request = models.ForeignKey('PullRequests', models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     comment_id = models.TextField()
#     position = models.IntegerField(blank=True, null=True)
#     body = models.CharField(max_length=256, blank=True, null=True)
#     commit = models.ForeignKey(Commits, models.DO_NOTHING)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'pull_request_comments'


# class PullRequestCommits(models.Model):
#     pull_request = models.ForeignKey('PullRequests', models.DO_NOTHING)
#     commit = models.ForeignKey(Commits, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'pull_request_commits'
#         unique_together = (('pull_request', 'commit'),)


# class PullRequestHistory(models.Model):
#     pull_request = models.ForeignKey('PullRequests', models.DO_NOTHING)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)
#     action = models.CharField(max_length=255)
#     actor = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pull_request_history'


# class PullRequests(models.Model):
#     head_repo = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)
#     base_repo = models.ForeignKey(Projects, models.DO_NOTHING)
#     head_commit = models.ForeignKey(Commits, models.DO_NOTHING, blank=True, null=True)
#     base_commit = models.ForeignKey(Commits, models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     pullreq_id = models.IntegerField()
#     intra_branch = models.IntegerField()
#     merged = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'pull_requests'
#         unique_together = (('pullreq_id', 'base_repo'),)


# class RepoLabels(models.Model):
#     repo = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(max_length=24)
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'repo_labels'


# class RepoMilestones(models.Model):
#     repo = models.ForeignKey(Projects, models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(max_length=24)
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'repo_milestones'

# class Users(models.Model):
#     login = models.CharField(unique=True, max_length=255)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     company = models.CharField(max_length=255, blank=True, null=True)
#     location = models.CharField(max_length=255, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)
#     type = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'users'


# class Watchers(models.Model):
#     repo = models.ForeignKey(Projects, models.DO_NOTHING)
#     user = models.ForeignKey(Users, models.DO_NOTHING)
#     created_at = models.DateTimeField()
#     ext_ref_id = models.CharField(max_length=24)

#     class Meta:
#         managed = False
#         db_table = 'watchers'
#         unique_together = (('repo', 'user'),)
