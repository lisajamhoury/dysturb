# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0008_auto_20151128_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='twilionumber',
            name='verified_cid',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
