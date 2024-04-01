from itertools import compress


def test_compress__len_numbers_eq_len_selectors() -> None:
    # Arrange
    numbers = [1, 2, 3, 4, 5]
    selectors = [True, True, False, False, False]

    # Act
    result = list(compress(numbers, selectors))

    # Assert
    assert result == [1, 2]


def test_compress__len_numbers_gt_len_selectors() -> None:
    # Arrange
    numbers = [1, 2, 3, 4, 5]
    selectors = [False, True]

    # Act
    result = list(compress(numbers, selectors))

    # Assert
    assert result == [2]


def test_compress__len_numbers_lt_len_selectors() -> None:
    # Arrange
    numbers = [1, 2]
    selectors = [False, False, True]

    # Act
    result = list(compress(numbers, selectors))

    # Assert
    assert result == []
