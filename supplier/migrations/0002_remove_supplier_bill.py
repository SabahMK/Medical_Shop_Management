# Generated by Django 3.0.2 on 2020-01-30 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='bill',
        ),
    ]
