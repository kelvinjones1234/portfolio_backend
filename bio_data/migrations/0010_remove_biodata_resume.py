# Generated by Django 5.1.4 on 2025-01-15 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bio_data", "0009_biodata_resume"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="biodata",
            name="resume",
        ),
    ]
