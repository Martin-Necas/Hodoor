# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 16:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0006_auto_20160417_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('key_type', models.CharField(blank=True, max_length=4, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='swipe',
            name='source',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]