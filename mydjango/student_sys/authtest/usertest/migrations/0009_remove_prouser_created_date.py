# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertest', '0008_auto_20190920_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prouser',
            name='created_date',
        ),
    ]
