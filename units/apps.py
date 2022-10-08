from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UnitsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "units"

    def ready(self) -> None:
        super().ready()
        from units import signals
        self.verbose_name = _("units")
