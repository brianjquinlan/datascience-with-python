# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-02 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library', models.CharField(max_length=250)),
                ('section', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]
