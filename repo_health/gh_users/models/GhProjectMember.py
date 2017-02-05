"""
GitHub project member.
"""

from django.db import models as m

class GhProjectMember(m.Model):
    repo = m.ForeignKey('gh_projects.GhProject', m.DO_NOTHING)
    user = m.ForeignKey('gh_users.GhUser', m.DO_NOTHING)
    created_at = m.DateTimeField()
    ext_ref_id = m.CharField(max_length=24, primary_key=True)

    def __str__(self):
        return self.user.login

    class Meta:
        managed = False
        db_table = 'project_members'
        unique_together = (('repo', 'user'),)
        verbose_name = 'GitHub Project Member'
