# Generated by Django 3.0.3 on 2020-12-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grbs', '0020_auto_20201209_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='grb',
            name='pcc',
            field=models.FloatField(blank=True, help_text='Probability of belonging to host galaxy', null=True, verbose_name='Probability of belonging to host galaxy'),
        ),
    ]
