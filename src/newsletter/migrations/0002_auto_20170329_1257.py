# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='city_name',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='zipcode',
        ),
    ]
