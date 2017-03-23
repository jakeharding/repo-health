"""
ResponseSerializer.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializers for api response.
"""


from rest_framework import serializers as s
from .MetricFieldSerializer import MetricFieldSerializer


class ResponseSerializer(s.Serializer):

    _metrics = None
    charts = s.SerializerMethodField()
    metrics = s.SerializerMethodField()

    def __init__(self, repo_data_dict):
        super().__init__(repo_data_dict)
        self._metrics = []
        for k, v in repo_data_dict.items():
            self._metrics.append(MetricFieldSerializer(v).data)
            # Do what is need to build the chart response here.

    # TODO Implement charts in response
    def get_charts(self, obj):
        return []

    def get_metrics(self, obj):
        return self._metrics
