# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0011_auto_20200316_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.PositiveIntegerField(verbose_name='性别', default=1, choices=[('男', 1), ('女', 2)]),
        ),
    ]
