# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('enaled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PollItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=200, blank=True, null=True)),
                ('vote', models.PositiveIntegerField(default=0)),
                ('poll', models.ForeignKey(to='mainsite.Poll')),
            ],
        ),
    ]
