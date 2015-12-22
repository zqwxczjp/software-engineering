# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_course_picurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForwardCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True)),
                ('courseinfo', models.ForeignKey(to='mainapp.Course')),
                ('user', models.ForeignKey(to='mainapp.User')),
            ],
        ),
    ]
