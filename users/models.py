from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from units.models import Unit
from users import managers


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    name: str = models.CharField(verbose_name=_("nome"), max_length=200)
    username: str = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email: str = models.CharField(verbose_name=_("email"), max_length=100)
    phone_number: str = models.CharField(verbose_name=_("telefone"), max_length=20)
    is_staff: bool = models.BooleanField(
        verbose_name=_("membro de equipe"),
        default=False,
    )
    integration_code: str = models.CharField(
        verbose_name=_("código de integração"),
        max_length=50,
        default="",
        blank=True,
    )
    units: models.QuerySet[Unit] = models.ManyToManyField(to="units.Unit")
    objects: managers.UserManager = managers.UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name"]

    class Meta:
        verbose_name = _("usuário")

    def __str__(self) -> str:
        return self.name
