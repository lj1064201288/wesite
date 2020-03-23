# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200320_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='正文', help_text='正文必须为markdown格式'),
        ),
    ]
