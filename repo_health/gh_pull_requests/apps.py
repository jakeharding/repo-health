'''
apps.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Set app name for admin.
'''

from django.apps import AppConfig


class GhPullRequestsConfig(AppConfig):
    name = 'repo_health.gh_pull_requests'
    verbose_name = 'GitHub Pull requests'
