from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "yumgo_python_template"

    verbose_name = _("Yumgo python Template")
