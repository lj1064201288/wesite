# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='content',
            field=models.TextField(verbose_name='内容', blank=True, help_text='如果设置的不是HTML类型， 可为空'),
        ),
    ]
