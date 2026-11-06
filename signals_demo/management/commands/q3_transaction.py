from typing import Any

from django.core.management.base import BaseCommand
from django.db import transaction

from signals_demo.models import Order, SignalLog
from signals_demo.signals import last_call


class Command(BaseCommand):
    help = "Q3: do signals run in the same database transaction as the caller?"

    def handle(self, *args: Any, **options: Any) -> None:
        last_call.clear()
        Order.objects.all().delete()
        SignalLog.objects.all().delete()

        try:
            with transaction.atomic():
                Order.objects.create(item="monitor")
                self.stdout.write(
                    f"SignalLog rows inside the transaction: {SignalLog.objects.count()}"
                )
                raise RuntimeError("roll back")
        except RuntimeError:
            pass

        orders = Order.objects.count()
        logs = SignalLog.objects.count()
        self.stdout.write(f"Receiver in atomic block: {last_call['in_atomic_block']}")
        self.stdout.write(f"After rollback: {orders} orders, {logs} signal logs")

        if orders == 0 and logs == 0:
            self.stdout.write(
                self.style.SUCCESS("Same transaction: the receiver's write was rolled back too.")
            )
        else:
            self.stdout.write(self.style.ERROR("The receiver's write survived the rollback."))
