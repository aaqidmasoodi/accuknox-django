from django.test import SimpleTestCase

from .shapes import Rectangle


class RectangleTests(SimpleTestCase):
    def test_iteration(self):
        self.assertEqual(list(Rectangle(10, 5)), [{"length": 10}, {"width": 5}])

    def test_iterates_more_than_once(self):
        rect = Rectangle(3, 4)
        self.assertEqual(list(rect), list(rect))
