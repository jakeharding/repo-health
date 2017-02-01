'''
Github project commit.
'''

from django.db import models as m

class GhProjectCommit(m.Model):
    project = m.ForeignKey('gh_projects.GhProject', m.DO_NOTHING)
    commit = m.ForeignKey(Commits, m.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_commits'
        unique_together = (('project', 'commit'),)