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

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name="GitHub User"

    def __str__(self):
        return self.login