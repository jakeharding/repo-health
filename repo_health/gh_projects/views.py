"""
views.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Business logic for api endpoints.
"""


from django.db import models
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from repo_health.gh_pull_requests.serializers import GhPullRequestStatsSerializer
from repo_health.gh_issues.serializers import GhIssueStatsSerializer
from .models import GhProject
from .serializers import GhProjectSerializer


class GhProjectViewSet(ListModelMixin, GenericViewSet):
    queryset = GhProject.objects.all()
    serializer_class = GhProjectSerializer
    filter_fields = ('owner__login', 'name')

    def list(self, r, *args, **kwargs):
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

    @detail_route(methods=['GET'])
    def issues(self, *args, **kwargs):
        repo = GhProject.objects\
            .annotate(issues_count=models.Count('issues'))\
            .annotate(most_recent_issue_created=models.Max('issues__created_at'))\
            .annotate(labels_count=models.Count('labels'))\
            .prefetch_related('issues')\
            .prefetch_related('labels')\
            .get(pk=kwargs['pk'])

        ser = GhIssueStatsSerializer(repo)
        return Response(ser.data)
