# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0007_auto_20191005_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sku', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('images', models.URLField(null=True)),
                ('website', models.URLField(null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('category', models.ForeignKey(to='pollitem.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='poll',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pollitem',
            name='poll',
        ),
        migrations.DeleteModel(
            name='VoteCheck',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='PollItem',
        ),
    ]
