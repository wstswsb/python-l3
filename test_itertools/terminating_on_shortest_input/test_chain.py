from itertools import chain


def test_chain() -> None:
    # Act
    result = list(chain(range(3), range(2), (-1, -2)))

    # Assert
    assert result == [0, 1, 2, 0, 1, -1, -2]


def test_chain__from_iterable() -> None:
    # Act
    result = list(chain.from_iterable(["Name", "Surname"]))

    # Assert
    assert result == ["N", "a", "m", "e", "S", "u", "r", "n", "a", "m", "e"]
