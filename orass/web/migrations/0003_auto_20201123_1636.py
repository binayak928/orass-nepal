# Generated by Django 3.1.3 on 2020-11-23 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Blog',
        ),
    ]
