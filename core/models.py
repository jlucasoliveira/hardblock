from typing import Dict, Tuple
from uuid import uuid4
from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.constants import StatusKind
from core.managers import BaseManager


class BaseModel(models.Model):
    id: str = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status: str = models.CharField(
        choices=StatusKind.choices,
        default=StatusKind.ACTIVATED,
        max_length=15,
    )
    created_at: datetime = models.DateTimeField(
        verbose_name=_("data de criação"),
        auto_now_add=True,
    )
    updated_at: datetime = models.DateTimeField(
        verbose_name=_("data de atualização"),
        auto_now=True,
    )
    objects: BaseManager = BaseManager()

    class Meta:
        abstract = True
        ordering = ("created_at", )

    def delete(
        self,
        *args,
        hard_delete: bool = False,
        **kwargs,
    ) -> Tuple[int, Dict[str, int]] | None:

        if (hard_delete):
            return super().delete(*args, **kwargs)
        self.status = StatusKind.DELETED

        return self.save(update_fields=["status"])
