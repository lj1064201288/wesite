# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollitem',
            name='vote_user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
