# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-28 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_hostinfo_hostname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='HostName',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
