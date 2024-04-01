import operator
from itertools import accumulate


def test_accumulate__sum() -> None:
    # Arrange
    accumulator = accumulate(range(5), operator.add)

    # Act
    result = list(accumulator)

    # Assert
    assert result == [0, 1, 3, 6, 10]


def test_accumulate_initial() -> None:
    # Arrange
    accumulator = accumulate(range(5), operator.add, initial=10)

    # Act
    result = list(accumulator)

    # Assert
    assert len(result) == 6  # len(Iterable) + 1 (initial)
    assert result == [10, 10, 11, 13, 16, 20]
