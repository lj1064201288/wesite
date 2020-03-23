# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='用户名', max_length=30)),
                ('password', models.CharField(verbose_name='密码', max_length=30)),
                ('sex', models.CharField(verbose_name='性别', max_length=5, default=0, choices=[('男', 0), ('女', 1)])),
                ('height', models.PositiveIntegerField(verbose_name='身高', default=160)),
                ('weigh', models.PositiveIntegerField(verbose_name='体重')),
                ('created_date', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
