# Generated by Django 2.2 on 2020-11-15 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
                ('productname', models.CharField(max_length=50)),
                ('productdesc', models.TextField()),
                ('quanity', models.IntegerField()),
                ('location', models.CharField(blank=True, choices=[('CA', 'CA'), ('OH', 'OH'), ('WA', 'WA')], max_length=50)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('password', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_type', models.CharField(blank=True, choices=[('ADD', 'ADD'), ('REMOVE', 'REMOVE')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_user', to='ThereItIs_app.User')),
                ('updated_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_item', to='ThereItIs_app.Item')),
            ],
        ),
    ]