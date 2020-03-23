# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0013_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='updata_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
