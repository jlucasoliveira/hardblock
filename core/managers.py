from django.db.models import Model, Q, QuerySet, Manager
from core.constants import StatusKind


class BaseManager(Manager):
    def get_queryset(self) -> QuerySet[Model]:
        qs = super().get_queryset()
        qs = qs.filter(~Q(status=StatusKind.DELETED))
        return qs
