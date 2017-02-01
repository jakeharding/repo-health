'''
Hold the m for Github projects.
'''


from django.db import models as m

class GhProject(m.Model):
    url = m.CharField(max_length=255, blank=True, null=True)
    owner = m.ForeignKey('gh_users.GhUser', m.DO_NOTHING, blank=True, null=True)
    name = m.CharField(max_length=255)
    description = m.CharField(max_length=255, blank=True, null=True)
    language = m.CharField(max_length=255, blank=True, null=True)
    created_at = m.DateTimeField()
    ext_ref_id = m.CharField(max_length=24)
    forked_from = m.ForeignKey('self', m.DO_NOTHING, db_column='forked_from', blank=True, null=True)
    deleted = m.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'projects'
        unique_together = (('name', 'owner'),)
        verbose_name="GitHub Project"
