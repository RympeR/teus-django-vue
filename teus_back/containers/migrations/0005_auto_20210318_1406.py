# Generated by Django 3.1.7 on 2021-03-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0004_auto_20210316_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproposition',
            name='status',
            field=models.CharField(choices=[('в работе', 'в работе'), ('в архиве', 'в архиве'), ('выполнен', 'выполнен'), ('удален', 'удален')], default='в работе', max_length=20),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='status',
            field=models.CharField(choices=[('в работе', 'в работе'), ('в архиве', 'в архиве'), ('выполнен', 'выполнен'), ('удален', 'удален')], default='в работе', max_length=20),
        ),
    ]
