import functools
from collections.abc import Iterable
from typing import Any

import pytest


class Numbers:
    def __init__(self, sequence: Iterable[int]):
        self.numbers = tuple(sequence)

    def __eq__(self, other: Any) -> bool:
        return self.numbers == getattr(other, "numbers", ())

    def __gt__(self, other: Any) -> bool:
        return len(self.numbers) > len(getattr(other, "numbers", ()))


def test_numbers__compare_without_total_ordering() -> None:
    # Arrange
    numbers = Numbers(range(4))

    # Assert
    assert numbers < Numbers(range(5))
    assert numbers == Numbers(range(4))
    assert numbers > Numbers(range(3))

    with pytest.raises(TypeError):
        assert numbers <= Numbers(range(4))  # type: ignore
    with pytest.raises(TypeError):
        assert numbers >= Numbers(range(4))  # type: ignore


def test_numbers__compare_with_total_ordering() -> None:
    # Arrange
    DecoratedNumbers = functools.total_ordering(Numbers)
    numbers = DecoratedNumbers(range(4))

    # Assert
    assert numbers < Numbers(range(5))
    assert numbers == Numbers(range(4))
    assert numbers > Numbers(range(3))
    assert numbers <= Numbers(range(4))  # type: ignore
    assert numbers >= Numbers(range(4))  # type: ignore
