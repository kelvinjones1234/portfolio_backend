# Generated by Django 5.1.4 on 2025-01-15 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bio_data", "0008_remove_biodata_resume"),
    ]

    operations = [
        migrations.AddField(
            model_name="biodata",
            name="resume",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
