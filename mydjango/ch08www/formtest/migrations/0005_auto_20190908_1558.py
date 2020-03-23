# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formtest', '0004_auto_20190908_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='del_pass',
            field=models.CharField(max_length=10, default=123456),
        ),
    ]
