# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS_System', '0003_auto_20170404_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrisisState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crisisStateData', models.TextField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='reportdata',
            name='crisisState',
        ),
    ]