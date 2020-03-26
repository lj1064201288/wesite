# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_votecheck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='enaled',
            field=models.BooleanField(default=True),
        ),
    ]
