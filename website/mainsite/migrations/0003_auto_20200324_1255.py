# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20200324_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='created_date',
            new_name='created_at',
        ),
    ]
