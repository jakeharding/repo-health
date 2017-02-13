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
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_404_NOT_FOUND
from .models import GhProject


class GhProjectSerializer(ModelSerializer):
    class Meta:
        model = GhProject
        exclude = ['commits_m2m', 'maintainers', 'watchers', 'url', 'forked_from']
        

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
