# Generated by Django 3.2.9 on 2021-11-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hack4Music', '0010_auto_20211122_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(max_length=1200),
        ),
    ]