# Generated by Django 3.1 on 2020-12-01 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
       
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField( max_length=255,unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]