# Generated by Django 3.1.3 on 2020-11-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_event_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
