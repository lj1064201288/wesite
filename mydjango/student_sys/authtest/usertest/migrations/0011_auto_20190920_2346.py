# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0010_auto_20190920_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prouser',
            name='sex',
            field=models.CharField(max_length=5, default='男', choices=[('男', '男'), ('女', '女')]),
        ),
    ]
