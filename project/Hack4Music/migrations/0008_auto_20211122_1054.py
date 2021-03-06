# Generated by Django 3.2.9 on 2021-11-22 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hack4Music', '0007_auto_20211122_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 10, 54, 42, 510467)),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 10, 54, 42, 510183)),
        ),
        migrations.AlterField(
            model_name='release',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 10, 54, 42, 509909)),
        ),
        migrations.AlterField(
            model_name='video',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 10, 54, 42, 510717)),
        ),
    ]
