# Generated by Django 2.2.4 on 2022-06-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvShows_app', '0002_show_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(default=''),
        ),
    ]
