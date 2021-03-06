# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='UUID')),
            ],
            options={
                'verbose_name': 'Metric',
                'verbose_name_plural': 'Metrics',
            },
        ),
    ]
