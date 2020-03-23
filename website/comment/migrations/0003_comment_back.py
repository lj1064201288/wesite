# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20200315_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='back',
            field=models.CharField(verbose_name='博客地址', max_length=200, default=1),
            preserve_default=False,
        ),
    ]
