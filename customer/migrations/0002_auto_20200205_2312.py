# Generated by Django 3.0.2 on 2020-02-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=150, verbose_name='Phone'),
        ),
    ]
