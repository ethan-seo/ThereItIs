# Generated by Django 2.2 on 2020-11-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThereItIs_app', '0004_auto_20201120_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='ThereItIs_app/static/media/'),
        ),
    ]