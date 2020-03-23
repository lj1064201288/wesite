# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0010_auto_20191012_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='images',
            field=filer.fields.image.FilerImageField(related_name='product_image', to='filer.Image'),
        ),
    ]
