# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0009_remove_prouser_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prouser',
            name='sex',
            field=models.CharField(max_length=5, default=0, choices=[(0, '男'), (1, '女')]),
        ),
    ]
