# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0014_auto_20200319_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=mdeditor.fields.MDTextField(verbose_name='内容/消息'),
        ),
        migrations.AlterField(
            model_name='post',
            name='nickname',
            field=models.CharField(verbose_name='昵称', max_length=20, default=''),
        ),
    ]
