# Generated by Django 3.0.3 on 2022-05-15 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0005_auto_20220515_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedetailinfo',
            name='file_upload',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='filedetailinfo',
            name='guest_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
