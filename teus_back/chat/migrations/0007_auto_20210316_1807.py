# Generated by Django 3.1.7 on 2021-03-16 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20210316_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Чат', 'verbose_name_plural': 'Чаты'},
        ),
        migrations.RemoveField(
            model_name='chat',
            name='date',
        ),
        migrations.RemoveField(
            model_name='room',
            name='date',
        ),
    ]
