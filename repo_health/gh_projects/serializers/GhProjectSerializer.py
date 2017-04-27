"""
GhProjectSerializer.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Serializer for a GitHub repo.
"""

from rest_framework.serializers import Serializer, SerializerMethodField
from repo_health.gh_users.models import GhUser
from repo_health.metrics.serializers import MetricField


class GhProjectSerializer(Serializer):
    """
    Calculates the metrics for a repo. Each field returns a list corresponding to the fields of the FieldSerializer.

    """
    _contribs_count = None
    _watch_not_contribs_count = None
    _orgs_of_contribs_count = None
    _labels_count = None
    _commits_count = None
    _latest_commit = None

    # Currently no charts for the details
    _charts = []

    # Fields found directly on the model
    language = SerializerMethodField()
    name = SerializerMethodField()
    description = SerializerMethodField()
    forked_from = SerializerMethodField()
    created_at = SerializerMethodField()

    # Fields with calculations/aggregations
    contribs_count = SerializerMethodField()
    watchers_count = SerializerMethodField()
    commits_count = SerializerMethodField()
    milestones_count = SerializerMethodField()
    latest_commit_created_at = SerializerMethodField()
    labels_count = SerializerMethodField()
    orgs_of_contribs_count = SerializerMethodField()
    owned_by_org = SerializerMethodField()
    forks_count = SerializerMethodField()

    @property
    def charts(self):
        return self._charts

    def __init__(self, *args, **kwargs):
        """
        Get some statistics for repo.
        """
        super().__init__(*args, **kwargs)
        repo = args[0]
        if repo is not None:
            commits = (repo.commits_m2m.all() | repo.commits_fk.all()).order_by('-created_at')
            commit_users = GhUser.objects.filter(authored_commits__in=commits).distinct()
            self._commits_count = commits.count()
            self._contribs_count = commit_users.count()
            self._latest_commit = commits.first().created_at
            self._orgs_of_contribs_count = GhUser.objects.filter(members__in=commit_users).exclude(id=repo.owner.id).count()

    def get_language(self, repo):
        return MetricField(True, 'Language', 2, None, repo.language)

    def get_name(self, repo):
        return MetricField(True, None, 0, None, repo.name)

    def get_description(self, repo):
        return MetricField(True, None, 1, None, repo.description)

    def get_forked_from(self, repo):
        return MetricField(True, 'Has upstream', 3, None, repo.forked_from.name if repo.forked_from else None)

    def get_created_at(self, repo):
        return MetricField(True, 'Created at', 4, None, repo.created_at, True)

    def get_orgs_of_contribs_count(self, repo):
        return MetricField(True, "Number of outside organizations with commits", 5, None, self._orgs_of_contribs_count)

    def get_contribs_count(self, obj):
        return MetricField(True, 'Number of contributors', 6, None, self._contribs_count)
        
    def get_commits_count(self, obj):
        return MetricField(True, 'Number of commits', 7, None, self._commits_count)

    def get_maintainers_count(self, repo):
        return MetricField(True, 'Number of maintainers', 8, None, repo.maintainers.count())
    
    def get_watchers_count(self, repo):
        return MetricField(True, 'Number of watchers', 9, None, repo.watchers.count())

    def get_milestones_count(self, repo):
        return MetricField(True, 'Number of milestones', 10, None, repo.milestones.count())
    
    def get_latest_commit_created_at(self, repo):
        return MetricField(True, 'Age of latest commit', 11, None, self._latest_commit, True)
    
    def get_labels_count(self, repo):
        return MetricField(True, 'Number of labels', 12, None, repo.labels.count())
    
    def get_owned_by_org(self, repo):
        return MetricField(True, 'Is owner an organization', 13, None, repo.is_owned_by_org())
    
    def get_forks_count(self, repo):
        return MetricField(True, 'Number of forks', 14, None, repo.forks.all().count())
