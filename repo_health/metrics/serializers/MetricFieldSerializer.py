"""
FieldSerializer.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Model the field in the serializer for now. Possible we store this in the database at some point in the future.
"""


from rest_framework import serializers as s


class MetricField(object):
    is_displayed = display_name = ordering = chart_name = raw_data = None

    def __init__(self, is_displayed, display_name, ordering, chart_name, raw_data):
        self.is_displayed = is_displayed
        self.display_name = display_name
        self.ordering = ordering
        self.chart_name = chart_name
        self.raw_data = raw_data


class MetricFieldSerializer(s.Serializer):

    is_displayed = s.BooleanField()
    display_name = s.CharField()
    ordering = s.IntegerField()
    chart_name = s.CharField()
    raw_data = s.SerializerMethodField()

    def get_raw_data(self, obj):
        return obj.raw_data
