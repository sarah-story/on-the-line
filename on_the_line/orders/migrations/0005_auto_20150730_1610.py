# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20150730_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
