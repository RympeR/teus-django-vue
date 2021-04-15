# Generated by Django 3.1.7 on 2021-04-14 15:04

from django.db import migrations
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0007_merge_20210414_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='handshake_time',
            field=unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userproposition',
            name='end_date',
            field=unixtimestampfield.fields.UnixTimeStampField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='userproposition',
            name='start_date',
            field=unixtimestampfield.fields.UnixTimeStampField(blank=True, null=True, verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='end_date',
            field=unixtimestampfield.fields.UnixTimeStampField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='request_date',
            field=unixtimestampfield.fields.UnixTimeStampField(blank=True, null=True, verbose_name='date'),
        ),
    ]
