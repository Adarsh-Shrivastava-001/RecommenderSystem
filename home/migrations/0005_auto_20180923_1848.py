# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-23 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180923_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilesamazon',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mobilesflipkart',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mobilessnapdeal',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
