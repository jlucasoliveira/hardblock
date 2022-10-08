from django.db.models.signals import post_save
from django.dispatch import receiver

from attendant import models as attendant_models
from units import models


@receiver(post_save, sender=models.Unit)
def create_shared_counter_after_unit_creation(sender, instance, created = False, *args, **kwargs) -> None:
    if created:
        models.Counter.objects.create_shared_counter(instance.pk)


@receiver(post_save, sender=models.Unit)
def create_general_priority(sender, instance, created = False, *args, **kwargs):
    if created:
        attendant_models.Priority.objects.create_general_priority(instance.pk)
