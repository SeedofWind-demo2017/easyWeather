# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20170329_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='gender',
            field=models.CharField(default=b'', max_length=255, choices=[(None, b''), (b'F', b'Female'), (b'M', b'Male'), (b'O', b'Other')]),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
