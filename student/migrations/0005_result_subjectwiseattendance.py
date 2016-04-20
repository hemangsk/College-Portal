# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20160418_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marksInSubject1', models.IntegerField(default=0)),
                ('marksInSubject2', models.IntegerField(default=0)),
                ('marksInSubject3', models.IntegerField(default=0)),
                ('marksInSubject4', models.IntegerField(default=0)),
                ('marksInSubject5', models.IntegerField(default=0)),
                ('enrol', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubjectWiseAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.IntegerField(default=0)),
                ('subject2', models.IntegerField(default=0)),
                ('subject3', models.IntegerField(default=0)),
                ('subject4', models.IntegerField(default=0)),
                ('subject5', models.IntegerField(default=0)),
                ('enrol', models.IntegerField()),
            ],
        ),
    ]