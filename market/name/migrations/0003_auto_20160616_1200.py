# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0002_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biddingevent',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='biddingevent',
            name='starting_bid',
            field=models.FloatField(default=1.0),
        ),
    ]
