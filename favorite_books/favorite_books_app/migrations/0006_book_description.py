# Generated by Django 2.2.4 on 2022-06-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0005_auto_20220627_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
