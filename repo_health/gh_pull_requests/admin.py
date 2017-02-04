'''
admin.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Register models in admin.
'''

from django.contrib import admin as a
from repo_health.index.admin import ReadOnlyAdmin
from .models import *


a.site.register(GhPullRequest, ReadOnlyAdmin)
a.site.register(GhPullRequestComment, ReadOnlyAdmin)
a.site.register(GhPullRequestHistory, ReadOnlyAdmin)
