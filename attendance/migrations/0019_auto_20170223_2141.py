# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0018_auto_20160609_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
