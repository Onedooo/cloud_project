# Generated by Django 3.0.3 on 2022-05-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedetailinfo',
            name='file_url',
            field=models.FileField(blank=True, upload_to='directory/'),
        ),
        migrations.AlterField(
            model_name='filedetailinfo',
            name='guest_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_num',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
