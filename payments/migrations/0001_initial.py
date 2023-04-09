# Generated by Django 4.1.7 on 2023-04-08 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reservations", "0002_alter_reservation_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("payment_date", models.DateTimeField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("Card", "Kart"), ("Cash", "Nakit")], max_length=30
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservations.reservation",
                    ),
                ),
            ],
        ),
    ]