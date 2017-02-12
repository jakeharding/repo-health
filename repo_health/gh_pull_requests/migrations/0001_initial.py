# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GhPullRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pullreq_id', models.IntegerField()),
                ('intra_branch', models.IntegerField()),
                ('merged', models.IntegerField()),
            ],
            options={
                'managed': False,
                'verbose_name': 'GitHub Pull Request',
                'db_table': 'pull_requests',
            },
        ),
        migrations.CreateModel(
            name='GhPullRequestComment',
            fields=[
                ('comment_id', models.TextField()),
                ('position', models.IntegerField(blank=True, null=True)),
                ('body', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField()),
                ('ext_ref_id', models.CharField(max_length=24, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'verbose_name': 'GitHub Pull Request Comment',
                'db_table': 'pull_request_comments',
            },
        ),
        migrations.CreateModel(
            name='GhPullRequestCommit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'pull_request_commits',
            },
        ),
        migrations.CreateModel(
            name='GhPullRequestHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('ext_ref_id', models.CharField(max_length=24)),
                ('action', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'verbose_name': 'GitHub Pull Request History',
                'db_table': 'pull_request_history',
            },
        ),
    ]