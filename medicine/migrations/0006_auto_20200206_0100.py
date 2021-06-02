# Generated by Django 3.0.2 on 2020-02-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0005_auto_20200206_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='Description',
        ),
        migrations.AddField(
            model_name='medicine',
            name='body',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Body'),
        ),
    ]