# Generated by Django 4.1 on 2022-08-09 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
