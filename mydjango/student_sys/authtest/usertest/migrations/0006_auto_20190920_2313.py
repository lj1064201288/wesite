# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0005_prouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prouser',
            name='created_date',
            field=models.TimeField(auto_now=True),
        ),
    ]
