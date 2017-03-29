"""
TotalAndOpenLabelSerial.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Serializer for labels to provide the total issues of the label and the issues open with the label.
"""

from rest_framework import serializers as s
from ..models import GhIssueEvent


class TotalAndOpenIssueLabelSerial(s.Serializer):
    total = s.SerializerMethodField()
    open = s.SerializerMethodField()

    def get_total(self, label):
        return label.issues.count()

    def get_open(self, label):
        return label.issues.exclude(events__action=GhIssueEvent.CLOSED_ACTION).count()
