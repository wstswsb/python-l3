from itertools import combinations_with_replacement


def test_combinations_with_replacement() -> None:
    # Arrange
    iterable = [5, 6, 7, 8]

    # Act
    result = combinations_with_replacement(iterable, 2)

    # Assert
    assert next(result) == (5, 5)
    assert next(result) == (5, 6)
    assert next(result) == (5, 7)
    assert next(result) == (5, 8)

    assert next(result) == (6, 6)
    assert next(result) == (6, 7)
    assert next(result) == (6, 8)

    assert next(result) == (7, 7)
    assert next(result) == (7, 8)

    assert next(result) == (8, 8)
