import threading
from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order, SignalLog

# What the receiver saw on its last run, so callers can compare it with their own state.
last_call: dict[str, Any] = {}


@receiver(post_save, sender=Order)
def order_saved(sender: type[Order], instance: Order, created: bool, **kwargs: Any) -> None:
    last_call["thread_id"] = threading.get_ident()

    SignalLog.objects.create(message=f"Order {instance.pk} saved")
