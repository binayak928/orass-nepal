# Generated by Django 3.1.3 on 2020-11-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20201124_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestedDonor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=70)),
            ],
        ),
    ]