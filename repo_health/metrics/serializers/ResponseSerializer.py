"""
ResponseSerializers.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializers for api response.
"""


from rest_framework import serializers as s


class ResponseSerializer(s.Serializer):

    charts = s.SerializerMethodField()
    metrics = s.SerializerMethodField()

    def get_charts(self, obj):
        return []

    def get_metrics(self, obj):
        return []