# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '__first__'),
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='user',
            field=models.ForeignKey(default='', to='logininfo.CustomUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pollitem',
            name='image_url',
            field=models.CharField(max_length=500, blank=True, null=True),
        ),
    ]
