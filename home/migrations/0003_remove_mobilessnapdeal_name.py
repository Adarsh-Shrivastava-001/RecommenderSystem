# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-23 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180923_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobilessnapdeal',
            name='name',
        ),
    ]