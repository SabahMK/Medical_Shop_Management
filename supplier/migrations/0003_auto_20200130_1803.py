# Generated by Django 3.0.2 on 2020-01-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_remove_supplier_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='stock',
        ),
        migrations.AddField(
            model_name='supplier',
            name='contact_person',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Contact Person'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Num'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Company'),
        ),
    ]
