# Generated by Django 3.1.3 on 2020-11-23 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20201123_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]