# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollitem', '0006_auto_20190925_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('userid', models.PositiveIntegerField()),
                ('pollid', models.PositiveIntegerField()),
                ('vote_time', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='pollitem',
            name='images_url',
            field=models.ImageField(blank=True, upload_to='pollitem/static/user_images'),
        ),
    ]
