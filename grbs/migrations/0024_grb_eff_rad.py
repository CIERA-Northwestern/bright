# Generated by Django 3.0.3 on 2021-02-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grbs', '0023_auto_20210212_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='grb',
            name='eff_rad',
            field=models.FloatField(blank=True, help_text='eff_rad', null=True, verbose_name='eff_rad'),
        ),
    ]
