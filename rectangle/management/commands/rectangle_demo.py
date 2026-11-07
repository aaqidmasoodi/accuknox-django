from argparse import ArgumentParser
from typing import Any

from django.core.management.base import BaseCommand

from rectangle.shapes import Rectangle


class Command(BaseCommand):
    help = "Iterate over a Rectangle"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("length", type=int, nargs="?", default=10)
        parser.add_argument("width", type=int, nargs="?", default=5)

    def handle(self, *args: Any, **options: Any) -> None:
        rect = Rectangle(options["length"], options["width"])
        for item in rect:
            self.stdout.write(str(item))
