# Generated by Django 3.1.7 on 2021-04-15 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 0, 20), verbose_name='Expires at'),
        ),
    ]