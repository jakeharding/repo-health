"""
ChartSerializer.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Model data around a chart in the UI.
"""


from rest_framework import serializers as s


class ChartSerializer(s.Serializer):
    chart_type = s.IntegerField()
    label = s.CharField()
    x_names = s.SerializerMethodField()
