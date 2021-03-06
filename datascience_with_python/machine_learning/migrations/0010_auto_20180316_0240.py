# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0009_auto_20180316_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm',
            name='slug',
            field=models.SlugField(default='ok', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='slug',
            field=models.SlugField(default='ok', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pythonlibrary',
            name='slug',
            field=models.SlugField(default='ok', max_length=250),
            preserve_default=False,
        ),
    ]
