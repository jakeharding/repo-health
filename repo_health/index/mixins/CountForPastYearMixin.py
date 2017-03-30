"""
CountForPastYearMixin.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding

Provides some utility methods and constants for filtering a queryset for the past year into a list of integers of the
number of occurrences for each month.
"""


import datetime
import calendar
from django.db.models import F


class CountForPastYearMixin(object):
    ONE_YEAR = datetime.timedelta(days=366)

    def get_count_list_for_year(self, queryset, query_string='created_at'):
        """
        Builds a list of occurrences per month using the string provided for Django style filtering.
        Assume query_string=`created_at` if not supplied.
        Will get the most recent occurrence of the queryset based on the query_string and get the previous year's
        occurrences from that date.
        :param queryset: Django queryset. Members are assumed to have a created_at field
        :param query_string: String used with Django style filtering
        :return: 12 element list of the number of occurrences per month
        """

        count_for_year = []

        if queryset.exists():
            most_recent = queryset.order_by(F(query_string).desc()).first().created_at
            dt_to_filter = most_recent - self.ONE_YEAR
            for mon in range(12):
                qwargs = {
                    query_string + '__year': dt_to_filter.year,
                    query_string + '__month': dt_to_filter.month

                }
                days_in_mon = calendar.monthrange(dt_to_filter.year, dt_to_filter.month)[1]
                count_for_year.append(queryset.filter(**qwargs).count())
                dt_to_filter += datetime.timedelta(days=days_in_mon)
        return count_for_year
