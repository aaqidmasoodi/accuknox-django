import threading
import time

from django.test import TestCase

from .models import Order
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
