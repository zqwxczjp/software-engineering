# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_sendmesg'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmesg',
            name='HasRead',
            field=models.BooleanField(default=False),
        ),
    ]
