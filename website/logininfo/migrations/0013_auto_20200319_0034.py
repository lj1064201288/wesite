# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0012_auto_20200319_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.PositiveIntegerField(verbose_name='性别', default=1, choices=[(1, '男'), (2, '女')]),
        ),
    ]
