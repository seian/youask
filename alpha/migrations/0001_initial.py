# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celeb_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('birth', models.DateTimeField()),
                ('group', models.CharField(max_length=500)),
                ('job', models.CharField(max_length=500)),
                ('school', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Celeb_info_career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('_from', models.DateTimeField()),
                ('_to', models.DateTimeField()),
                ('award', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('nick_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=512)),
                ('signup_date', models.DateTimeField(auto_now=True)),
                ('contents', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('thread', models.IntegerField()),
                ('content', models.CharField(max_length=500)),
                ('preference', models.IntegerField()),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('parent_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('topic', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('post_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
