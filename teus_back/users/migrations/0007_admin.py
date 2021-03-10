# Generated by Django 3.1.7 on 2021-03-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210309_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Админ',
                'verbose_name_plural': 'Админы',
            },
        ),
    ]