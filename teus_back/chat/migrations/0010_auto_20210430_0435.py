# Generated by Django 3.1.7 on 2021-04-30 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210430_0435'),
        ('chat', '0009_auto_20210316_1812'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chat',
            unique_together={('date', 'user', 'room')},
        ),
    ]
