# Generated by Django 3.2.9 on 2021-11-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hack4Music', '0009_auto_20211122_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_at',
            field=models.DateField(default='2021-11-22'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='published_at',
            field=models.DateField(default='2021-11-22'),
        ),
        migrations.AlterField(
            model_name='release',
            name='release_date',
            field=models.DateField(default='2021-11-22'),
        ),
        migrations.AlterField(
            model_name='video',
            name='published_at',
            field=models.DateField(default='2021-11-22'),
        ),
    ]
