# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formtest', '0002_auto_20190908_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mood',
            field=models.ForeignKey(verbose_name='选择心情', to='formtest.Mood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
