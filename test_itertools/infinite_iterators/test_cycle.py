from collections.abc import Iterator
from itertools import cycle

_GEN_CALLS = 0


def numbers_gen() -> Iterator[int]:
    global _GEN_CALLS
    numbers = (1, 2, 3, 4)
    for n in numbers:
        yield n
        _GEN_CALLS += 1


def test_cycle__saves_copies_inside() -> None:
    # Arrange
    global _GEN_CALLS
    _GEN_CALLS = 0

    # Act
    result = []
    for item in cycle(numbers_gen()):
        result.append(item)
        if result == [1, 2, 3, 4, 1, 2, 3, 4]:
            break

    # Assert
    assert _GEN_CALLS == 4
