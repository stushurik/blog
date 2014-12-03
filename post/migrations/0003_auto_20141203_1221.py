# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20141203_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short_body',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
            preserve_default=True,
        ),
    ]
