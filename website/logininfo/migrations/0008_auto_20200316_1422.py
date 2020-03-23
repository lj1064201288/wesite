# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0007_auto_20200316_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.PositiveIntegerField(verbose_name='身高（cm）', default=160),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='website',
            field=models.URLField(verbose_name='个人网站', null=True),
        ),
    ]
