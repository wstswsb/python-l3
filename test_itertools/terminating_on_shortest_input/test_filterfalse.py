from itertools import filterfalse


def test_filterfalse() -> None:
    # Arrange
    items = (1, -2, 3, -4)

    # Act
    result = list(filterfalse(lambda item: item > 0, items))

    # Assert
    assert result == [-2, -4]
