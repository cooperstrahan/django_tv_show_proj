# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-19 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tv_show', '0002_showmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShowManager',
        ),
    ]
