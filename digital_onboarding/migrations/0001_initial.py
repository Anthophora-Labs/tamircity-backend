# Generated by Django 4.1.7 on 2023-04-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TechServiceCandidate",
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
                ("service_name", models.CharField(max_length=150)),
                ("business_type", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=250)),
                ("number_of_branches", models.IntegerField()),
                ("number_of_technicians", models.IntegerField()),
                ("name", models.CharField(max_length=150)),
                ("surname", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=150)),
                ("phone_number", models.CharField(max_length=15)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Cancelled", "Cancelled"),
                            ("Approved", "Approved"),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-id"],},
        ),
    ]
