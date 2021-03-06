# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('template', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
