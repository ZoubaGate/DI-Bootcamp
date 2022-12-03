# Generated by Django 4.1.2 on 2022-10-26 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('URL', models.URLField()),
                ('uploader_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 10, 26, 14, 27, 19, 50361))),
                ('category', models.ManyToManyField(blank=True, related_name='categories', to='mygifs.category')),
            ],
        ),
    ]
