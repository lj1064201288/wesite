# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0006_auto_20200316_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='height',
            field=models.PositiveIntegerField(default=160),
        ),
        migrations.AddField(
            model_name='customuser',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
