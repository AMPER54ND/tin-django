# Generated by Django 2.1.10 on 2019-12-12 01:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Beer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("brewery", models.CharField(max_length=200)),
                ("beer_type", models.CharField(max_length=200)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user", models.CharField(max_length=200)),
                (
                    "rating",
                    models.IntegerField(
                        default=5,
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ],
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("comment", models.CharField(blank=True, max_length=256)),
                ("public", models.BooleanField(default=False)),
                (
                    "beer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rate_beer.Beer"
                    ),
                ),
            ],
        ),
    ]
