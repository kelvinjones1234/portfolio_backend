from django.apps import AppConfig


class ProjectDataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "project_data"

    verbose_name = 'Projects'
