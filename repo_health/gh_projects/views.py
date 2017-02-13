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
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_404_NOT_FOUND
from repo_health.gh_users.models import GhUser
from .models import GhProject



class GhProjectSerializer(ModelSerializer):
    _contribs_count = None
    _watchers_count = None
    _watch_not_contribs_count = None
    _orgs_of_contribs_count = None
    _labels_count = None
    _commits_count = None
    _milestones_count = None
    _latest_commit = None

    contribs_count = SerializerMethodField()
    watchers_count = SerializerMethodField()
    # watch_not_contribs_count = SerializerMethodField()
    # commits_count = SerializerMethodField()
    # milestones_count = SerializerMethodField()
    # labels_count = SerializerMethodField()
    # orgs_of_contribs_count = SerializerMethodField()
    # commits_count = SerializerMethodField()
    

    def __init__(self, *args, **kwargs):
        """
        Get some statistics for repo.
        """
        super().__init__(*args, **kwargs)
        repo = args[0].first()
        if repo is not None:
            commits = repo.commits_m2m.all() | repo.commits_fk.all()
            self._commits_count = commits.count()
            self._contribs_count = GhUser.objects.filter(commits__in=commits).distinct().count()
            # print (dir(repo))
            self._watchers_count = repo.ghwatcher_set.count()

    def get_watchers_count(self, obj):
        return self._watchers_count

    def get_contribs_count(self, obj):
        return self._contribs_count
        
    class Meta:
        model = GhProject
        exclude = ['commits_m2m', 'maintainers', 'watchers', 'url',]
        

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
