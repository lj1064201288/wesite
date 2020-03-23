# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('sku', models.IntegerField()),
                ('qty', models.PositiveIntegerField()),
                ('size', models.CharField(max_length=1, choices=[('S', 'Small'), ('M', 'Mudium'), ('L', 'Large')])),
            ],
        ),
    ]
