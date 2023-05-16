# Generated by Django 4.2 on 2023-05-05 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("libray", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignedbook",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]