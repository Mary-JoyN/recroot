from django.apps import AppConfig


class RecruitmentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.recruitment"

    def ready(self):
        from .signals import create, emails, permissions
