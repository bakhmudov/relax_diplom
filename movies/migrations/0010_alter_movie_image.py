# Generated by Django 4.2.1 on 2023-05-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='static/admin/img/'),
        ),
    ]
