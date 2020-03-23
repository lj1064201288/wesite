# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20200315_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='内容', blank=True, help_text='如果设置的不是HTML类型， 可为空'),
        ),
    ]
