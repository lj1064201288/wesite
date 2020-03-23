# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0007_auto_20190920_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prouser',
            name='created_date',
            field=models.TimeField(auto_created=datetime.datetime(2019, 9, 20, 23, 15, 2, 718929)),
        ),
    ]
