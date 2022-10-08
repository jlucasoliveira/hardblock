from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusKind(models.TextChoices):
    DELETED = ("DELETED", _("Removido"))
    DEACTIVATED = ("DEACTIVATED", _("Desativado"))
    ACTIVATED = ("ACTIVATED", _("Ativado"))
