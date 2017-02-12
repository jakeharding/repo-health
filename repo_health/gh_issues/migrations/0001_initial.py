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
            name='GhIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_id', models.TextField()),
                ('pull_request', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('ext_ref_id', models.CharField(max_length=24)),
            ],
            options={
                'managed': False,
                'verbose_name': 'GitHub Issue',
                'db_table': 'issues',
            },
        ),
        migrations.CreateModel(
            name='GhIssueComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('ext_ref_id', models.CharField(max_length=24)),
            ],
            options={
                'managed': False,
                'verbose_name': 'GitHub Issue Comment',
                'db_table': 'issue_comments',
            },
        ),
        migrations.CreateModel(
            name='GhIssueEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.TextField()),
                ('action', models.CharField(max_length=255)),
                ('action_specific', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField()),
                ('ext_ref_id', models.CharField(max_length=24)),
            ],
            options={
                'managed': False,
                'verbose_name': 'GitHub Issue Event',
                'db_table': 'issue_events',
            },
        ),
        migrations.CreateModel(
            name='GhIssueLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'issue_labels',
            },
        ),
    ]