# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0003_auto_20190925_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollitem',
            name='images_url',
            field=models.ImageField(blank=True, upload_to='statc'),
        ),
    ]
