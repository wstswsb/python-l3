from itertools import groupby


def test_groupby__unsorted() -> None:
    # Arrange
    animals = ["cat", "dog", "cow", "cat", "elephant", "dog", "cat"]

    # Act
    groups: list[list[str]] = []
    keys: list[str] = []
    for key, group in groupby(animals):
        keys.append(key)
        groups.append(list(group))

    # Assert
    assert groups == [
        ["cat"],
        ["dog"],
        ["cow"],
        ["cat"],
        ["elephant"],
        ["dog"],
        ["cat"],
    ]
    assert keys == animals


def test_groupby__sorted() -> None:
    # Arrange
    animals = ["cat", "dog", "cat", "elephant", "dog", "cat"]

    # Act
    groups: list[list[str]] = []
    keys: list[str] = []

    def key_func(item: str) -> str:
        return item[:2]

    animals.sort(key=key_func)
    for key, group in groupby(animals, key_func):
        keys.append(key)
        groups.append(list(group))

    assert keys == ["ca", "do", "el"]
    assert groups == [["cat", "cat", "cat"], ["dog", "dog"], ["elephant"]]
