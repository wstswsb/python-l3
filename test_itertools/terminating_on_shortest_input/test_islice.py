from itertools import islice

import pytest


def test_islice__iterable_stop() -> None:
    # Arrange
    iterable = "ABCDEFG"
    stop = 3

    # Act
    result = islice(iterable, stop)

    # Assert
    assert next(result) == "A"
    assert next(result) == "B"
    assert next(result) == "C"
    with pytest.raises(StopIteration):
        next(result)


def test_islice__iterable_start_stop() -> None:
    # Arrange
    iterable = "ABCDEFG"
    start = 2
    stop = 4

    # Act
    result = islice(iterable, start, stop)

    # Assert
    assert next(result) == "C"
    assert next(result) == "D"
    with pytest.raises(StopIteration):
        next(result)


def test_islice__iterable_start_stop_step() -> None:
    # Arrange   0123456
    iterable = "ABCDEFG"
    start = 2
    stop = 999_999
    step = 3

    # Act
    result = islice(iterable, start, stop, step)

    # Assert
    assert next(result) == "C"
    assert next(result) == "F"

    with pytest.raises(StopIteration):
        next(result)
