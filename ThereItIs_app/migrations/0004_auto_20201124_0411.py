# Generated by Django 2.2 on 2020-11-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThereItIs_app', '0003_auto_20201123_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(blank=True, choices=[('Add New Item', 'Add New Item'), ('Add Stock', 'Add Stock'), ('Remove', 'Remove')], max_length=50),
        ),
    ]
