# Generated by Django 2.2.12 on 2020-04-16 00:42

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_semester_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markrange',
            name='days',
            field=models.CharField(default='1,2,3,4,5,6,7', help_text='Comma seperated list of weekdays that this range is active, where Monday=1 and Sunday=7.                    E.g.: "1,3,5" for M, W, F.', max_length=13, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
