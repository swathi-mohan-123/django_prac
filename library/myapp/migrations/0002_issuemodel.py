# Generated by Django 4.2 on 2023-05-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="issuemodel",
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
                ("bookid", models.IntegerField()),
                ("bookname", models.CharField(max_length=500)),
                ("bookdesc", models.CharField(max_length=500)),
                ("studid", models.IntegerField()),
                ("studname", models.CharField(max_length=100)),
            ],
        ),
    ]