# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20151026_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.IntegerField(default=-1, blank=True),
            preserve_default=False,
        ),
    ]
