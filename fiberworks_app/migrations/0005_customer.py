# Generated by Django 4.2.6 on 2023-10-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiberworks_app', '0004_alter_product_description_alter_product_in_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]