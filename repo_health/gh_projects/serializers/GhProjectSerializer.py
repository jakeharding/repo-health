"""
serializers.py - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  J. Harding
  
Serializer for a GitHub repo.
"""

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from repo_health.gh_users.models import GhUser
from ..models import GhProject


class GhProjectSerializer(ModelSerializer):
    _contribs_count = None
    _watch_not_contribs_count = None
    _orgs_of_contribs_count = None
    _labels_count = None
    _commits_count = None
    _latest_commit = None

    contribs_count = SerializerMethodField()
    watchers_count = SerializerMethodField()
    commits_count = SerializerMethodField()
    milestones_count = SerializerMethodField()
    latest_commit_created_at = SerializerMethodField()
    labels_count = SerializerMethodField()
    orgs_of_contribs_count = SerializerMethodField()
    owned_by_org = SerializerMethodField()
    forks_count = SerializerMethodField()    

    def __init__(self, *args, **kwargs):
        """
        Get some statistics for repo.
        """
        super().__init__(*args, **kwargs)
        repo = args[0].first()
        if repo is not None:
            commits = (repo.commits_m2m.all() | repo.commits_fk.all()).order_by('-created_at')
            commit_users = GhUser.objects.filter(commits__in=commits).distinct()
            self._commits_count = commits.count()
            self._contribs_count = commit_users.count()
            self._latest_commit = commits.first().created_at
            self._orgs_of_contribs_count = GhUser.objects.filter(members__in=commit_users).exclude(id=repo.owner.id).count()

    def get_orgs_of_contribs_count(self, repo):
        return self._orgs_of_contribs_count

    def get_contribs_count(self, obj):
        return self._contribs_count
        
    def get_commits_count(self, obj):
        return self._commits_count

    def get_maintainers_count(self, repo):
        return repo.maintainers.count()
    
    def get_watchers_count(self, repo):
        return repo.watchers.count()

    def get_milestones_count(self, repo):
        return repo.milestones.count()
    
    def get_latest_commit_created_at(self, repo):
        return self._latest_commit
    
    def get_labels_count(self, repo):
        return repo.labels.count()
    
    def get_owned_by_org(self, repo):
        return repo.is_owned_by_org()
    
    def get_forks_count(self, repo):
        return repo.forks.all().count()
        
    class Meta:
        model = GhProject
        exclude = ['commits_m2m', 'maintainers', 'watchers', 'url', 'forks', ]
