# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_snippet_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
