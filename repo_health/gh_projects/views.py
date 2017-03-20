"""
views.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Business logic for api endpoints.
"""


from django.db import models
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from repo_health.gh_pull_requests.serializers import GhPullRequestStatsSerializer
from .models import GhProject
from .serializers import GhProjectSerializer, StatsUrlsSerializer


class GhProjectViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = GhProject.objects.all()
    serializer_class = StatsUrlsSerializer
    filter_fields = ('owner__login', 'name')

    def retrieve(self, r, *args, **kwargs):
        """
        Override to use the correct serializer. Otherwise it would use the stats serializer.
        get_object method returns a 404 if project is not found.
        :param r: Request object
        :param args: pk of project is the first arg
        :param kwargs:
        :return: Response
        """
        obj = self.get_object()
        return Response(GhProjectSerializer(obj).data)

    def list(self, r, *args, **kwargs):
        """
        Temporary override as we may use this method to filter repos for an autocomplete.
        :param r: Request for repo
        :param args:
        :param kwargs:
        :return: Response
        """
        if not r.GET.get('name') or not r.GET.get('owner__login'):
            raise NotFound('Repo not found', HTTP_404_NOT_FOUND)
        response = super().list(r, *args, **kwargs)
        if len(response.data) is not 1:
            raise NotFound('Repo not found', HTTP_404_NOT_FOUND)
        else:
            response.data = response.data[0]
        return response

    @detail_route(url_path='pull-requests')
    def pull_requests(self, *args, **kwargs):
        repo = GhProject.objects\
            .annotate(pr_count=models.Count('prs_to'))\
            .get(pk=kwargs['pk'])

        pr_stats = GhPullRequestStatsSerializer(repo)
        return Response(pr_stats.data)
