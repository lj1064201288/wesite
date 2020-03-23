# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usertest', '0004_auto_20190920_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sex', models.CharField(max_length=5, default=0, choices=[('0', '男'), ('1', '女')])),
                ('height', models.PositiveIntegerField(verbose_name='身高(cm)', default=160)),
                ('weigh', models.PositiveIntegerField(verbose_name='体重(kg)')),
                ('created_date', models.TimeField(auto_now_add=True)),
                ('website', models.URLField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
