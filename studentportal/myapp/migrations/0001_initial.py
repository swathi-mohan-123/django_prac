# Generated by Django 4.2 on 2023-05-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="studentmodel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("student_number", models.PositiveIntegerField()),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("field_of_study", models.CharField(max_length=100)),
                ("gpa", models.FloatField()),
            ],
        ),
    ]
