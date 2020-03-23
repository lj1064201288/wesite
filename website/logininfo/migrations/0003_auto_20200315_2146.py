# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0002_user_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='enabled',
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(verbose_name='是否激活', default=False),
        ),
    ]
