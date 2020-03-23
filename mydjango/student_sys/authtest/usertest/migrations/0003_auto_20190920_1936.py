# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0002_auto_20190920_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.PositiveIntegerField(verbose_name='身高(cm)', default=160),
        ),
        migrations.AlterField(
            model_name='user',
            name='weigh',
            field=models.PositiveIntegerField(verbose_name='体重(kg)'),
        ),
    ]
