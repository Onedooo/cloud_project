# Generated by Django 3.0.3 on 2022-05-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0006_auto_20220515_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedetailinfo',
            name='file_url',
            field=models.FileField(null=True, upload_to='directory/'),
        ),
    ]