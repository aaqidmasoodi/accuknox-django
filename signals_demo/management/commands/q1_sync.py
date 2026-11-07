import time
from typing import Any

from django.core.management.base import BaseCommand

from signals_demo.models import Order
from signals_demo.signals import HANDLER_DELAY, last_call


class Command(BaseCommand):
    help = "Q1: are signals synchronous by default?"

    def handle(self, *args: Any, **options: Any) -> None:
        last_call.clear()
        last_call["slow"] = True

        start = time.perf_counter()
        Order.objects.create(item="keyboard")
        end = time.perf_counter()

        self.stdout.write(f"Receiver sleeps for {HANDLER_DELAY}s")
        self.stdout.write(f"save() returned after {end - start:.2f}s")
        self.stdout.write(
            f"Receiver finished before save() returned: {last_call['finished_at'] <= end}"
        )

        if end - start >= HANDLER_DELAY:
            self.stdout.write(
                self.style.SUCCESS("Synchronous: the caller waited for the receiver.")
            )
        else:
            self.stdout.write(self.style.ERROR("Asynchronous: the caller did not wait."))
