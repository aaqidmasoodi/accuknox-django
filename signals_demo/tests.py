import threading
import time

from django.db import transaction
from django.test import TestCase, TransactionTestCase

from .models import Order, SignalLog
from .signals import HANDLER_DELAY, last_call


class SignalBehaviourTests(TestCase):
    def setUp(self):
        last_call.clear()

    def test_signal_is_synchronous(self):
        last_call["slow"] = True
        start = time.perf_counter()
        Order.objects.create(item="keyboard")
        end = time.perf_counter()

        self.assertGreaterEqual(end - start, HANDLER_DELAY)
        self.assertLessEqual(last_call["finished_at"], end)

    def test_signal_runs_in_caller_thread(self):
        Order.objects.create(item="mouse")
        self.assertEqual(last_call["thread_id"], threading.get_ident())


class SignalTransactionTests(TransactionTestCase):
    def test_signal_runs_in_caller_transaction(self):
        last_call.clear()
        with self.assertRaises(RuntimeError), transaction.atomic():
            Order.objects.create(item="monitor")
            raise RuntimeError("roll back")

        self.assertTrue(last_call["in_atomic_block"])
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(SignalLog.objects.count(), 0)
