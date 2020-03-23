# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sku', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('size', models.CharField(max_length=1, choices=[('S', 'Smaill'), ('M', 'Medium'), ('L', 'Large')])),
            ],
        ),
    ]
