from django.test import SimpleTestCase

from .shapes import Rectangle


class RectangleTests(SimpleTestCase):
    def test_iteration(self):
        self.assertEqual(list(Rectangle(10, 5)), [{"length": 10}, {"width": 5}])
