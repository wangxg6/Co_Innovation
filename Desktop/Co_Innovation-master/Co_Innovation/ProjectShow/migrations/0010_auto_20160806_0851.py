# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectShow', '0009_auto_20160806_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finish_time',
            field=models.DateTimeField(verbose_name=b'\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
