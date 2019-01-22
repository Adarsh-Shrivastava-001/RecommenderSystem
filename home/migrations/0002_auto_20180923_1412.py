# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-23 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='graph',
            field=models.ImageField(blank=True, upload_to='graph_image'),
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='image',
            field=models.ImageField(blank=True, upload_to='mobile_image'),
        ),
        migrations.AlterField(
            model_name='mobilesamazon',
            name='delivery',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mobilesamazon',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='mobilesflipkart',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='mobilessnapdeal',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]