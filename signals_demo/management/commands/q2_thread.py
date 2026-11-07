import threading
from typing import Any

from django.core.management.base import BaseCommand

from signals_demo.models import Order
from signals_demo.signals import last_call


class Command(BaseCommand):
    help = "Q2: do signals run in the same thread as the caller?"

    def handle(self, *args: Any, **options: Any) -> None:
        last_call.clear()

        caller_thread = threading.get_ident()
        Order.objects.create(item="mouse")

        self.stdout.write(f"Caller thread:   {caller_thread}")
        self.stdout.write(f"Receiver thread: {last_call['thread_id']}")

        if last_call["thread_id"] == caller_thread:
            self.stdout.write(self.style.SUCCESS("Same thread."))
        else:
            self.stdout.write(self.style.ERROR("Different threads."))
