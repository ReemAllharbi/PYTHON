# Generated by Django 2.2.4 on 2022-06-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvShows_app', '0003_auto_20220620_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='describtion',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]
