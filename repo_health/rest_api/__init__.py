"""
__init__.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Configure urls for rest api.
"""

from django.conf.urls import url, include
from rest_framework import routers
from repo_health.gh_projects.views import ProjectViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]