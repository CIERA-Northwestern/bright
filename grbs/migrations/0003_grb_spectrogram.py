# Generated by Django 3.0.3 on 2020-07-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grbs', '0002_auto_20200722_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='grb',
            name='spectrogram',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
