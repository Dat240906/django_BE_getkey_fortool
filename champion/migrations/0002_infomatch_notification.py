# Generated by Django 4.2.4 on 2023-08-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noti', models.CharField(default='Vui là 9, Thắng là 10.', max_length=255)),
            ],
        ),
    ]
