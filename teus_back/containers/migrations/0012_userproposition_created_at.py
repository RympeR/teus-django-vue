# Generated by Django 3.1.7 on 2021-05-05 07:13

from django.db import migrations
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0011_auto_20210420_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproposition',
            name='created_at',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True, null=True),
        ),
    ]
