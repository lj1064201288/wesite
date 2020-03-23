# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0019_auto_20200322_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='ddate',
            field=models.DateTimeField(verbose_name='发布时间', auto_now_add=True),
        ),
    ]
