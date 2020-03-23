# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formtest', '0005_auto_20190908_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='enabled',
            field=models.BooleanField(verbose_name='是否呈现出来', default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(verbose_name='内容/消息'),
        ),
        migrations.AlterField(
            model_name='post',
            name='nickname',
            field=models.CharField(verbose_name='昵称', max_length=20, default='一位不愿透露姓名的勇士'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_time',
            field=models.DateTimeField(verbose_name='发布时间', auto_now_add=True),
        ),
    ]
