# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='tags',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
