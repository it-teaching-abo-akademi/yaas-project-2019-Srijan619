# Generated by Django 2.2.5 on 2019-10-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='minimum_price',
            field=models.CharField(default=0.0, max_length=50),
        ),
    ]
