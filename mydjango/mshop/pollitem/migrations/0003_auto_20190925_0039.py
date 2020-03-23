# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0002_auto_20190924_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollitem',
            name='vote_user',
        ),
        migrations.AlterField(
            model_name='pollitem',
            name='images_url',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
