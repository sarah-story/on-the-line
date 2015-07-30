# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('items', models.TextField()),
                ('order_time', models.DateTimeField()),
                ('order_id', models.CharField(null=True, max_length=100)),
            ],
        ),
    ]
