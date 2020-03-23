# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0011_auto_20191012_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='images',
            new_name='image',
        ),
    ]
