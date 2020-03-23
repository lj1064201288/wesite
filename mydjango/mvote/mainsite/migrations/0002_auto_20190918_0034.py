# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollitem',
            name='image_url',
            field=models.CharField(max_length=500, blank=True, null=True),
        ),
    ]
