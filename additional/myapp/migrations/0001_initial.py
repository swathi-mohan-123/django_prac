# Generated by Django 4.2 on 2023-05-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="humanmodel",
            fields=[
                (
                    "fname",
                    models.CharField(
                        choices=[
                            ("Swathi", "Swathi"),
                            ("Murthy", "Murthy"),
                            ("Sakshi", "Sakshi"),
                            ("Chitti", "Chitti"),
                        ],
                        max_length=100,
                    ),
                ),
                ("lname", models.CharField(max_length=100)),
                ("phone", models.IntegerField(primary_key=True, serialize=False)),
                ("addr", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
            ],
        ),
    ]