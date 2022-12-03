# Generated by Django 4.1.2 on 2022-10-21 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='gifs',
        ),
        migrations.AddField(
            model_name='gifmodel',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='gifs.category'),
        ),
        migrations.AlterField(
            model_name='gifmodel',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 21, 13, 44, 16, 881591)),
        ),
    ]
