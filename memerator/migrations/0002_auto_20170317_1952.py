# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='meme',
            name='text',
            field=models.CharField(max_length=50),
        ),
    ]
