# Generated by Django 2.2.4 on 2022-06-16 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0006_dojos_ninjas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninjas',
            name='dojo_id',
        ),
        migrations.DeleteModel(
            name='dojos',
        ),
        migrations.DeleteModel(
            name='ninjas',
        ),
    ]
