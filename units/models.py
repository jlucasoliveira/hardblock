from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from units import managers


class Address(BaseModel):
    street: str = models.CharField(verbose_name=_("endereço"), max_length=150)
    number: str = models.CharField(verbose_name=_("número"), max_length=20)
    street_2: str = models.CharField(
        verbose_name=_("complemento"),
        max_length=150,
        blank=True,
    )
    district: str = models.CharField(verbose_name=_("bairro"), max_length=100)
    city: str = models.CharField(verbose_name=_("cidade"), max_length=150)
    state: str = models.CharField(verbose_name=_("estado"), max_length=5)
    zip_code: str = models.CharField(verbose_name=_("CEP"), max_length=15)

    class Meta:
        verbose_name = _("endereço")

    def __str__(self) -> str:
        return f"{self.street}, {self.number}, {self.district}, {self.city} - {self.state}"


class Unit(BaseModel):
    name: str = models.CharField(verbose_name=_("nome"), max_length=100)
    description: str = models.TextField(
        verbose_name=_("descrição"),
        max_length=200,
        blank=True,
    )
    phone_number: str = models.CharField(verbose_name=_("telefone"), max_length=20)
    integration_code: str = models.CharField(
        verbose_name=_("código de integração"),
        max_length=20,
    )
    address: Address = models.ForeignKey(
        to="units.Address",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("endereço"),
    )

    class Meta:
        verbose_name = _("unidade")

    def __str__(self) -> str:
        return self.name


class Counter(BaseModel):
    name: str = models.CharField(verbose_name=_("nome"), max_length=100)
    description: str = models.TextField(
        verbose_name=_("descrição"),
        max_length=200,
        blank=True,
    )
    unit: Unit = models.ForeignKey(
        to="units.Unit",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("unidade"),
    )
    attendance_amount: int = models.PositiveSmallIntegerField(
        verbose_name=_("quantidade de atendimento"),
    )
    shared: bool = models.BooleanField(verbose_name=_("uso compartilhado"), default=False)
    is_constrained_by_queue: bool = models.BooleanField(
        verbose_name=_("limitado as filas"),
        help_text=_("Chama somente as senhas de suas respectivas filas."),
        default=True,
    )
    priorities = models.ManyToManyField(
        to="attendant.Priority",
        verbose_name=_("prioridades"),
    )

    objects = managers.CounterManager()

    class Meta:
        verbose_name = _("guichê")

    def __str__(self) -> str:
        return self.name


class Room(BaseModel):
    name: str = models.CharField(verbose_name=_("nome"), max_length=100)
    description: str = models.TextField(
        verbose_name=_("descrição"),
        blank=True,
    )
    unit: Unit = models.ForeignKey(
        to="units.Unit",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("unidade"),
    )
    # TODO: Remove from change form
    busy: bool = models.BooleanField(verbose_name=_("ocupado"), default=False)
    shared: bool = models.BooleanField(verbose_name=_("uso compartilhado"), default=False)

    class Meta:
        verbose_name = _("ambiente")

    def __str__(self) -> str:
        return self.name
