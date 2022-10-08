from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AttendantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'attendant'

    def ready(self) -> None:
        super().ready()
        from attendant import signals
        self.verbose_name = _("attendant")
