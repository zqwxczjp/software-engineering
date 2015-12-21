# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20151220_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmesg',
            name='Time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
