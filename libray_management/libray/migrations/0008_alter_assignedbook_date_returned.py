# Generated by Django 4.2 on 2023-05-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("libray", "0007_alter_assignedbook_date_returned"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignedbook",
            name="date_returned",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
