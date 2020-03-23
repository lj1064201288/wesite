# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0016_post_message_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message_html',
            field=mdeditor.fields.MDTextField(verbose_name='markdown', blank=True, null=True, default=''),
        ),
    ]
