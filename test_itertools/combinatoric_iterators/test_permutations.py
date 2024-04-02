from itertools import permutations

import pytest


def test_permutations__without_length_of_permutation_item() -> None:
    # Arrange
    iterable = "ABC"

    # Act
    result = permutations(iterable)

    # Assert
    assert next(result) == ("A", "B", "C")
    assert next(result) == ("A", "C", "B")
    assert next(result) == ("B", "A", "C")
    assert next(result) == ("B", "C", "A")
    assert next(result) == ("C", "A", "B")
    assert next(result) == ("C", "B", "A")
    with pytest.raises(StopIteration):
        next(result)


def test_permutations__with_length_of_permutation_item() -> None:
    # Arrange
    iterable = "ABC"

    # Act
    result = permutations(iterable, r=2)

    # Assert
    assert next(result) == ("A", "B")
    assert next(result) == ("A", "C")
    assert next(result) == ("B", "A")
    assert next(result) == ("B", "C")
    assert next(result) == ("C", "A")
    assert next(result) == ("C", "B")
    with pytest.raises(StopIteration):
        next(result)
