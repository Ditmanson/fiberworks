# Generated by Django 4.2.6 on 2023-11-02 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiberworks_app', '0018_rename_intro_homescreen_paragraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_homepage',
            field=models.BooleanField(default=False),
        ),
    ]