"""
views.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  

Business logic for api endpoints.
"""




from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.serializers import ModelSerializer
from .models import GhProject


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = GhProject
        exclude = ['commits_m2m', 'maintainers', 'watchers',]
        


class ProjectViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = GhProject.objects.all()
    serializer_class = ProjectSerializer
