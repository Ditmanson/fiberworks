# Generated by Django 4.2.6 on 2023-11-02 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiberworks_app', '0016_alter_homescreen_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='homescreen',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
