# Generated by Django 3.0.2 on 2020-02-05 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200205_2312'),
        ('medicine', '0002_auto_20200203_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='content',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meds', to='customer.Customer', verbose_name='Get'),
        ),
    ]
