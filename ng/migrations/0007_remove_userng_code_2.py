# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-04 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ng', '0006_auto_20180704_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userng',
            name='code_2',
        ),
    ]
