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
            name='outbound_calling_override',
            field=models.CharField(help_text=b'Use this field to add an outbound calling number for shortcodes', max_length=20, blank=True),
        ),
    ]
