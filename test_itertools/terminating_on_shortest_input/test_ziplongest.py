from itertools import zip_longest


def test_zip_longest__defaults() -> None:
    # Arrange
    indexes = ["i1", "i2", "i3", "i4"]
    scores = ["s1", "s2", "s3"]

    # Act
    result = list(zip_longest(indexes, scores))

    # Assert
    assert result == [
        ("i1", "s1"),
        ("i2", "s2"),
        ("i3", "s3"),
        ("i4", None),
    ]


def test_zip_longest__custom_fillvalue() -> None:
    # Arrange
    indexes = ["i1", "i2", "i3", "i4"]
    scores = ["s1", "s2", "s3"]

    # Act
    result = list(zip_longest(indexes, scores, fillvalue="TEST"))

    # Assert
    assert result == [
        ("i1", "s1"),
        ("i2", "s2"),
        ("i3", "s3"),
        ("i4", "TEST"),
    ]
