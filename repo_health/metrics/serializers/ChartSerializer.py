"""
ChartSerializer.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Model data around a chart in the UI.
"""

import datetime
from rest_framework import serializers as s


class ChartField(object):
    chart_name = None
    chart_type = None
    most_recent = None
    title = None
    x_label = None
    y_label = None

    def __init__(self, chart_name, most_recent, title, x_label, y_label, chart_type):
        """
        Model data for a chart.
        :param chart_name: string: Name of chart
        :param most_recent: datetime: Most recent datetime of data in chart
        :param title: string: Title of chart
        :param x_label: string: Label of the x axis
        :param y_label: string: Label of the y axis
        """
        self.chart_name = chart_name
        self.most_recent = most_recent
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.chart_type = chart_type


class ChartSerializer(s.Serializer):
    chart_type = s.IntegerField()
    x_names = s.SerializerMethodField()
    y_names = s.SerializerMethodField()
    title = s.CharField()
    x_label = s.CharField()
    y_label = s.CharField()

    def get_x_names(self, obj):
        names = []
        if obj.most_recent and isinstance(obj.most_recent, datetime.datetime):
            dt = obj.most_recent
            for m in range(12):
                names.insert(0, dt.strftime('%b'))
                dt = (dt.replace(day=1) - datetime.timedelta(days=1))
        return names

    def get_y_names(self, obj):
        return []