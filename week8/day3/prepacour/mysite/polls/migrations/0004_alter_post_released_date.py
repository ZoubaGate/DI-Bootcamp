# Generated by Django 4.1.2 on 2022-10-19 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_imageprofile_alter_post_released_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 19, 14, 14, 44, 22802)),
        ),
    ]
