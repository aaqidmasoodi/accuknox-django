from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order, SignalLog


@receiver(post_save, sender=Order)
def order_saved(sender: type[Order], instance: Order, created: bool, **kwargs: Any) -> None:
    SignalLog.objects.create(message=f"Order {instance.pk} saved")
