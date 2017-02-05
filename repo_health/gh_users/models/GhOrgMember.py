"""
GitHub Organization member.
"""

from django.db import models as m

class GhOrgMember(m.Model):
    org = m.ForeignKey('gh_users.GhUser', m.DO_NOTHING)
    user = m.ForeignKey('gh_users.GhUser', m.DO_NOTHING)
    created_at = m.DateTimeField()

    def __str__(self):
        return self.user.login

    class Meta:
        managed = False
        db_table = 'organization_members'
        unique_together = (('org', 'user'),)
        verbose_name = 'GitHub Organization Member'
