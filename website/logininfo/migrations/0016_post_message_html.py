# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0015_auto_20200322_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message_html',
            field=mdeditor.fields.MDTextField(verbose_name='markdown', default=''),
        ),
    ]
