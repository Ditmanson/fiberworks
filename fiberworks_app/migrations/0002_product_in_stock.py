# Generated by Django 4.2.6 on 2023-10-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiberworks_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
    ]
