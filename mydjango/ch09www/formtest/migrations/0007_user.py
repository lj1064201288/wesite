# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formtest', '0006_auto_20190911_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='用户名', max_length=20)),
                ('password', models.CharField(verbose_name='用户密码', max_length=20)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
    ]
