# Generated by Django 3.1.7 on 2021-03-16 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210316_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Send datetime'),
        ),
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
    ]
