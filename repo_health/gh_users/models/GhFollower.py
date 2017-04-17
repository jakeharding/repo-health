"""
Github Follower
"""

from django.db import models as m


class GhFollower(m.Model):
    user = m.ForeignKey('gh_users.GhUser', m.DO_NOTHING)
    follower = m.ForeignKey('gh_users.GhUser', m.DO_NOTHING, related_name='follower')
    created_at = m.DateTimeField()
    ext_ref_id = m.CharField(max_length=24, primary_key=True)#Set this as primary key so django doesn't add the id field

    def __str__(self):
        return self.user.login

    class Meta:
        db_table = 'followers'
        unique_together = (('user', 'follower'),)
        verbose_name = "GitHub Follower"
