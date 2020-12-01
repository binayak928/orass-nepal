# Generated by Django 3.1.3 on 2020-12-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20201201_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('regDate', models.DateField(auto_now_add=True)),
                ('eventDate', models.DateField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
