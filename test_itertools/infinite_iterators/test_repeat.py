from itertools import repeat


def test_repeat__with_times() -> None:
    # Arrange
    repeater = repeat(None, 3)

    # Act
    result = list(repeater)

    # Assert
    assert result == [None, None, None]


def test_repeat__without_times_documentation_example() -> None:
    # Act
    result_repeat = list(map(pow, range(5), repeat(2)))

    # readable_equivalent
    result_readable = [pow(number, 2) for number in range(5)]

    # Assert
    assert result_repeat == result_readable
