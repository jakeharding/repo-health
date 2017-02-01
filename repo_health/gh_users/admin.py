'''
Register models with Django Admin.
'''

from django.contrib import admin as a
from repo_health.index.admin import ReadOnlyAdmin
from .models import *

a.site.register(GhUser, ReadOnlyAdmin)
a.site.register(GhFollower, ReadOnlyAdmin)
a.site.register(GhWatcher, ReadOnlyAdmin)
a.site.register(GhOrgMember, ReadOnlyAdmin)
a.site.register(GhProjectMember, ReadOnlyAdmin)
