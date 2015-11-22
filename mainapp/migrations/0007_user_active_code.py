# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_user_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active_code',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
