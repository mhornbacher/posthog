# Generated by Django 4.2.15 on 2024-11-20 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def add_default_themes(apps, schema_editor):
    DataColorTheme = apps.get_model("posthog", "DataColorTheme")

    DataColorTheme.objects.create(
        name="Default Theme",
        colors=[
            "#1d4aff",
            "#621da6",
            "#42827e",
            "#ce0e74",
            "#f14f58",
            "#7c440e",
            "#529a0a",
            "#0476fb",
            "#fe729e",
            "#35416b",
            "#41cbc4",
            "#b64b02",
            "#e4a604",
            "#a56eff",
            "#30d5c8",
        ],
    )


def remove_default_themes(apps, schema_editor):
    # no-op, as table will be dropped on rollback anyway
    pass


class Migration(migrations.Migration):
    dependencies = [("posthog", "0536_alertconfiguration_skip_weekend")]

    operations = [
        migrations.CreateModel(
            name="DataColorTheme",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("colors", models.JSONField(default=list)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posthog.team", null=True, blank=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
                ("deleted", models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.RunPython(add_default_themes, remove_default_themes),
        migrations.AddField(
            model_name="team",
            name="default_data_theme",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
