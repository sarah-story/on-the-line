# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='complete',
            name='phone',
            field=models.CharField(null=True, max_length=11),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(null=True, max_length=11),
        ),
    ]
