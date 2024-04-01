from itertools import dropwhile


def test_dropwhile() -> None:
    # Arrange
    items = [1, "A", 1.1, None, "r1", b"r2"]

    # Act
    result = list(dropwhile(lambda item: item is not None, items))

    # Assert
    assert result == [None, "r1", b"r2"]
