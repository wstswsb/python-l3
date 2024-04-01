from itertools import count


def test_count__int_defaults() -> None:
    # Arrange
    counter = count()

    # Act
    result = [next(counter) for _ in range(5)]

    # Assert
    assert result == [0, 1, 2, 3, 4]


def test_count__int_custom_start() -> None:
    # Arrange
    counter = count(start=5)

    # Act
    result = [next(counter) for _ in range(5)]

    # Assert
    assert result == [5, 6, 7, 8, 9]


def test_count__int_custom_start_step() -> None:
    # Arrange
    counter = count(start=5, step=10)

    # Act
    result = [next(counter) for _ in range(5)]

    # Assert
    assert result == [5, 15, 25, 35, 45]


def test_count_float_default_step() -> None:
    # Arrange
    counter = count(0.1)

    # Act
    result = [next(counter) for _ in range(5)]

    # Assert
    assert result == [0.1, 1.1, 2.1, 3.1, 4.1]


def test_count_float_custom_step() -> None:
    # Arrange
    counter = count(start=0.1, step=0.33)

    # Act
    result = [round(next(counter), 2) for _ in range(5)]

    # Assert
    assert result == [0.1, 0.43, 0.76, 1.09, 1.42]


def test_count_start_int_step_float() -> None:
    # Arrange
    counter = count(1, 0.1)

    # Act
    result = [round(next(counter), 2) for _ in range(3)]

    # Assert
    assert result == [1, 1.1, 1.2]


def test_count_start_float_step_int() -> None:
    # Arrange
    counter = count(0.1, 1)

    # Act
    result = [round(next(counter), 2) for _ in range(3)]

    # Assert
    assert result == [0.1, 1.1, 2.1]
