# Generated by Django 4.2 on 2023-05-15 03:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("libray", "0004_assignedbook_available_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="assignedbook",
            name="available_quantity",
        ),
    ]
