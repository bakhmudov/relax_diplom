# Generated by Django 4.2.1 on 2023-05-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_showtime_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='time',
            field=models.CharField(max_length=5),
        ),
    ]
