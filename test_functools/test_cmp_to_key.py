from functools import cmp_to_key


def cmp_asc(first: int, second: int) -> int:
    if first > second:
        return 1
    elif first < second:
        return -1
    return 0


def cmp_desc(first: int, second: int) -> int:
    if first > second:
        return -1
    elif first < second:
        return 1
    return 0


def test_cmp_to_key__asc() -> None:
    # Arrange
    items_key = [4, 3, 2, 1]
    items_cmp = [4, 3, 2, 1]

    # Act
    items_key.sort()
    items_cmp.sort(key=cmp_to_key(cmp_asc))

    # Assert
    assert items_key == items_cmp == [1, 2, 3, 4]


def test_cmp_to_key__desc() -> None:
    # Arrange
    items_key = [1, 2, 3, 4]
    items_cmp = [1, 2, 3, 4]

    # Act
    items_key.sort(key=lambda item: -item)
    items_cmp.sort(key=cmp_to_key(cmp_desc))

    # Assert
    assert items_key == items_cmp == [4, 3, 2, 1]
