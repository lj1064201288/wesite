# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0018_auto_20200322_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='budget',
            field=models.FloatField(verbose_name='今日花费', default=0),
        ),
        migrations.AlterField(
            model_name='diary',
            name='ddate',
            field=models.DateField(verbose_name='发布时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='note',
            field=mdeditor.fields.MDTextField(verbose_name='内容/消息'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='weight',
            field=models.FloatField(verbose_name='身高', default=0),
        ),
    ]
