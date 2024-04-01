from itertools import batched


def test_batched() -> None:
    # Arrange
    sequence = (1, 2, 3, 4, 5)

    # Act
    result = list(batched(sequence, 2))

    # Assert
    assert result == [(1, 2), (3, 4), (5,)]
