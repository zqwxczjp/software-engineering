# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_sendmesg_hasread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
