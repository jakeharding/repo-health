"""
views.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Business logic for api endpoints.
"""

from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_404_NOT_FOUND
from repo_health.gh_users.models import GhUser
from .models import GhProject
from .serializers import GhProjectSerializer


class GhProjectViewSet(ListModelMixin, GenericViewSet):
    queryset = GhProject.objects.all()
    serializer_class = GhProjectSerializer
    filter_fields = ('owner__login', 'name')

    def list(self, r, *args, **kwargs):
        response  = super().list(r, *args, **kwargs)
        if len(response.data) is not 1:
            raise NotFound('Repo not found', HTTP_404_NOT_FOUND)
        else:
            response.data = response.data[0]
        return response
