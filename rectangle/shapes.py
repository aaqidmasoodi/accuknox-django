from collections.abc import Iterator


class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def __iter__(self) -> Iterator[dict[str, int]]:
        yield {"length": self.length}
        yield {"width": self.width}
