from itertools import product

import pytest


def test_product__1_iterable() -> None:
    # Act
    result = product("01")

    # Assert
    assert next(result) == ("0",)
    assert next(result) == ("1",)
    with pytest.raises(StopIteration):
        next(result)


def test_product__2_iterable() -> None:
    # Act
    result = product("abc", [1, 2])

    # Assert
    assert next(result) == ("a", 1)
    assert next(result) == ("a", 2)
    assert next(result) == ("b", 1)
    assert next(result) == ("b", 2)
    assert next(result) == ("c", 1)
    assert next(result) == ("c", 2)
    with pytest.raises(StopIteration):
        next(result)


def test_product__repeat() -> None:
    # Act
    result = product("ab", repeat=2)

    # Assert
    assert next(result) == ("a", "a")
    assert next(result) == ("a", "b")
    assert next(result) == ("b", "a")
    assert next(result) == ("b", "b")
