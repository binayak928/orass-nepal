# Generated by Django 3.1.3 on 2020-11-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201124_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]