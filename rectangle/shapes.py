from collections.abc import Iterator


class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("length and width must be integers")
        self.length = length
        self.width = width

    def __iter__(self) -> Iterator[dict[str, int]]:
        yield {"length": self.length}
        yield {"width": self.width}
