"""
views.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Business logic for api endpoints.
"""


import datetime, calendar
from django.utils import timezone
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from repo_health.gh_users.models import GhUser
from repo_health.gh_pull_requests.models import GhPullRequestHistory
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
    
    @detail_route(url_path='pull-requests')
    def pull_requests(self, *args, **kwargs):
        repo = self.get_object()
        one_year = datetime.timedelta(days=366)
        
        opened_histories = GhPullRequestHistory.objects.filter(
            pull_request__base_repo = repo, 
            action = GhPullRequestHistory.OPENED_ACTION,
        ).order_by('-created_at')
        most_recent_history_created = opened_histories.first().created_at

        opened_prev_year = opened_histories.filter(created_at__gte=most_recent_history_created - one_year).distinct()
        dt_to_filter = opened_prev_year.last().created_at

        opened_count_for_year = []
        for m in range(12):
            days_in_mon = calendar.monthrange(dt_to_filter.year, dt_to_filter.month)[1]
            opened_count_for_year.append(opened_prev_year.filter(
                created_at__year=dt_to_filter.year,                
                created_at__month=dt_to_filter.month).count())
            dt_to_filter += datetime.timedelta(days = days_in_mon)
        print (opened_count_for_year)
        return Response(HTTP_200_OK)

        
