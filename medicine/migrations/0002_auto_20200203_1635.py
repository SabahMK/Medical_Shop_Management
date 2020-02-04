# Generated by Django 3.0.2 on 2020-02-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='bill',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='weight',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Weight'),
        ),
    ]