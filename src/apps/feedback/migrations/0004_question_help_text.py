# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-27 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20180419_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='help_text',
            field=models.CharField(blank=True, max_length=100, verbose_name='Help text'),
        ),
    ]