'''
apps.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Setup app config for Django.
'''

from django.apps import AppConfig


class GhCommitsConfig(AppConfig):
    name = 'repo_health.gh_commits'
    verbose_name = 'Github Commits'