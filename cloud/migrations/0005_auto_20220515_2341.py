# Generated by Django 3.0.3 on 2022-05-15 14:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0004_auto_20220515_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedetailinfo',
            name='file_upload',
            field=models.DateField(default=datetime.datetime(2022, 5, 15, 14, 41, 49, 971855, tzinfo=utc)),
        ),
    ]
