# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_learning', '0010_auto_20180316_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/commands/'),
        ),
        migrations.AddField(
            model_name='dataframe',
            name='libraries',
            field=models.ManyToManyField(to='machine_learning.Library'),
        ),
    ]