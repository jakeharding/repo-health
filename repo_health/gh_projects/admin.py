'''
Register models in admin.
'''

from django.contrib import admin as a
from repo_health.index.admin import ReadOnlyAdmin

from .models import *


a.site.register(GhProject, ReadOnlyAdmin)
