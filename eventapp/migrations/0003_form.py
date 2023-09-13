# Generated by Django 4.2.5 on 2023-09-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventapp", "0002_event_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Form",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("email", models.CharField(max_length=120)),
                ("phoneno", models.CharField(max_length=120)),
            ],
        ),
    ]
