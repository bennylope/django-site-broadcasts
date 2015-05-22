# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=140)),
                ('start_time', models.DateTimeField(help_text=b'Optional, used to start showing a message in the\n            future', null=True, blank=True)),
                ('end_time', models.DateTimeField(help_text=b'When this message should\n            expire')),
                ('is_published', models.BooleanField(default=True, verbose_name=b'Published?')),
            ],
            options={
                'ordering': ['-end_time'],
            },
        ),
    ]
