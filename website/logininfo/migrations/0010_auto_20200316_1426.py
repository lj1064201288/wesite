# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0009_auto_20200316_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='website',
            field=models.URLField(verbose_name='个人网站(可填)', blank=True, null=True),
        ),
    ]
