# Generated by Django 4.1.3 on 2022-11-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EconomicLessons",
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
                ("title", models.CharField(max_length=120)),
                ("genre", models.CharField(max_length=50)),
                ("picture", models.FileField(upload_to="")),
                (
                    "difficulty",
                    models.CharField(
                        choices=[("簡単", "簡単"), ("普通", "普通"), ("難しい", "難しい")],
                        max_length=10,
                    ),
                ),
                (
                    "keyword",
                    models.CharField(
                        choices=[("投資", "投資"), ("株式", "株式"), ("経済", "経済")],
                        max_length=10,
                    ),
                ),
                ("leaf_length", models.PositiveIntegerField()),
                ("detail", models.TextField()),
            ],
        ),
    ]
