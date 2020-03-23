# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0008_auto_20200316_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='website',
            field=models.URLField(verbose_name='个人网站', blank=True, null=True),
        ),
    ]
