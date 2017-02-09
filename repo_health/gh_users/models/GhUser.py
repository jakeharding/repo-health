from django.db import models as m


class GhUser(m.Model):
    login = m.CharField(unique=True, max_length=255)
    name = m.CharField(max_length=255, blank=True, null=True)
    company = m.CharField(max_length=255, blank=True, null=True)
    location = m.CharField(max_length=255, blank=True, null=True)
    email = m.CharField(max_length=255, blank=True, null=True)
    created_at = m.DateTimeField()
    ext_ref_id = m.CharField(max_length=24)
    type = m.CharField(max_length=255)

    #M2M Fields added.
    comment_commits = m.ManyToManyField(
        'gh_commits.GhCommit', 
        through='gh_commits.GhCommitComment'
    )
    # comment_issues = m.ManyToManyField(
    #     'gh_issues.GhIssue',
    #     through='gh_issues.GhIssueComment'
    # )
    organizations = m.ManyToManyField(
        'self', related_name='members',
        through='gh_users.GhOrgMember'
    )

    # watched_repos = m.ManyToManyField(
    #     'gh_projects.GhProject',
    #     through='gh_users.GhWatcher'
    # )
    # maintain_repos = m.ManyToManyField(
    #     'gh_projects.GhProject',
    #     through='gh_users.GhProjectMember'
    # )

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name="GitHub User"

    def __str__(self):
        return self.login
