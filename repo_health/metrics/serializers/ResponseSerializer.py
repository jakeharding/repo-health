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
from .ChartSerializer import ChartSerializer


class ResponseSerializer(s.Serializer):

    _metrics = None
    _charts = None
    charts = s.SerializerMethodField()
    metrics = s.SerializerMethodField()

    def __init__(self, metric_dict, charts):
        super().__init__(metric_dict)
        self._metrics = []
        self._charts = charts

    # TODO Implement charts in response
    def get_charts(self, obj):
        chart_data = {}
        for c in self._charts:
            chart_data[c.chart_name] = ChartSerializer(c).data
        return chart_data

    def get_metrics(self, obj):
        for k, v in obj.items():
            self._metrics.append(MetricFieldSerializer(v).data)
        return self._metrics
