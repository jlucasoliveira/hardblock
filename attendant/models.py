from datetime import datetime
from tabnanny import verbose
from typing import Counter

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from attendant.managers import PriorityManager
from core.models import BaseModel
from units.models import Room, Unit


class Priority(BaseModel):
    name: str = models.CharField(verbose_name=_("nome"), max_length=100)
    description: str = models.TextField(verbose_name=_("descrição"), max_length=150)
    abbreviation: str = models.CharField(verbose_name=_("sigla"), max_length=20)
    personalized_service: bool = models.BooleanField(
        verbose_name=_("atendimento personalizado"),
        default=True,
    )
    importance: float = models.FloatField(
        verbose_name=_("peso"),
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0),
        ],
    )
    units: models.QuerySet[Unit] = models.ManyToManyField(
        to="units.Unit",
        verbose_name=_("unidades"),
    )

    objects = PriorityManager()

    class Meta:
        verbose_name = _("prioridade")

    def __str__(self) -> str:
        return self.name

    @property
    def units_summary(self) -> str:
        return ", ".join(
            self.units.only("name").values_list("name", flat=True)
        )
    units_summary.fget.short_description = "unidades"


class Queue(BaseModel):
    priority = models.ForeignKey(
        to="attendant.Priority",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("prioridade"),
    )
    counter = models.ForeignKey(
        to="units.Counter",
        on_delete=models.deletion.  CASCADE,
        verbose_name=_("guichê"),
    )
    unit = models.ForeignKey(
        to="units.Unit",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("unidade"),
    )

    class Meta:
        verbose_name = _("fila")

    def __str__(self) -> str:
        return f"{self.priority} {self.counter} {self.unit}"


class Ticket(BaseModel):
    priority: Priority = models.ForeignKey(
        to="attendant.Priority",
        on_delete=models.PROTECT,
        verbose_name=_("prioridade"),
    )
    number: int = models.IntegerField(
        verbose_name=_("número"),
        validators=[MinValueValidator(1)],
    )
    unit: Unit = models.ForeignKey(
        to="units.Unit",
        on_delete=models.deletion.PROTECT,
        verbose_name=_("unidade"),
    )
    is_reactivated: bool = models.BooleanField(verbose_name=_("reativada"), default=False)
    times_called: int = models.IntegerField(verbose_name=_("vezes chamadas"), default=0)

    class Meta:
        verbose_name = _("senha")

    def __str__(self) -> str:
        return f"{self.priority.abbreviation.upper()}{self.number} em {self.unit}"


class TicketRelatedMixin(BaseModel):
    ticket = models.OneToOneField(
        to="attendant.Ticket",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("senha"),
    )
    counter: Counter = models.ForeignKey(
        to="units.Counter",
        on_delete=models.PROTECT,
        verbose_name=_("guichê"),
    )
    finished_at: datetime = models.DateTimeField(
        verbose_name=_("data de finalização"),
        null=True,
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.ticket} {self.created_at}"


class Call(TicketRelatedMixin):
    class Meta:
        verbose_name = _("chamada")


class Forwarding(TicketRelatedMixin):
    attendant = models.ForeignKey(
        to="users.User",
        on_delete=models.PROTECT,
        verbose_name=_("atendente"),
    )
    room: Room = models.ForeignKey(
        to="units.Room",
        on_delete=models.PROTECT,
        verbose_name=_("ambiente"),
    )
    start_at = models.DateTimeField(verbose_name=_("data de atendimento"), null=True)

    class Meta:
        verbose_name = _("encaminhamento")
