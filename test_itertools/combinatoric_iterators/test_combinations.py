from itertools import combinations


def test_combinations() -> None:
    # Arrange
    iterable = [5, 6, 7, 8]

    # Act
    result = combinations(iterable, 2)

    # Assert
    assert next(result) == (5, 6)
    assert next(result) == (5, 7)
    assert next(result) == (5, 8)

    assert next(result) == (6, 7)
    assert next(result) == (6, 8)

    assert next(result) == (7, 8)
