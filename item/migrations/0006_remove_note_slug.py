# Generated by Django 3.1 on 2020-12-10 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_note_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='slug',
        ),
    ]
