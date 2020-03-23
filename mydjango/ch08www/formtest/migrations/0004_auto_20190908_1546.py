# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formtest', '0003_auto_20190908_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
