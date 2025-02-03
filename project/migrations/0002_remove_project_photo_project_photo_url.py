# Generated by Django 5.1.5 on 2025-02-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="photo",
        ),
        migrations.AddField(
            model_name="project",
            name="photo_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
