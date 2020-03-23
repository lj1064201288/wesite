# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='话题', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('enabled', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PollItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('vote', models.PositiveIntegerField(default=0)),
                ('images_url', models.ImageField(null=True, upload_to='')),
                ('vote_user', models.CharField(max_length=50)),
                ('poll', models.ForeignKey(to='pollitem.Poll')),
            ],
        ),
    ]
