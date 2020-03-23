# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0017_auto_20200322_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='del_pass',
            field=models.CharField(max_length=10, blank=True, null=True, default=123456),
        ),
    ]
