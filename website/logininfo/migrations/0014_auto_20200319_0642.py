# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logininfo', '0013_auto_20200319_0034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mood',
            options={'verbose_name': '心情', 'verbose_name_plural': '心情'},
        ),
    ]
