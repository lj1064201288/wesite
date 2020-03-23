# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0009_auto_20191012_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='images',
            field=models.URLField(null=True),
        ),
    ]
