"""
Simple lightweight unbounded function cache.

implementation:

def cache(user_function, /):
    'Simple lightweight unbounded cache.  Sometimes called "memoize".'
    return lru_cache(maxsize=None)(user_function)
"""
from functools import cache
from typing import Any, Protocol


class HasComputedField(Protocol):
    @property
    def computed_field(self) -> str:
        ...


class ObjectWithoutCustomEqMethod:
    def __init__(self, field: str):
        self.field = field
        self.field_calls = 0

    @property
    def computed_field(self) -> str:
        self.field_calls += 1
        return self.field


class ObjectWithCustomEqMethod:
    def __init__(self, field: str):
        self.field = field
        self.field_calls = 0

    @property
    def computed_field(self) -> str:
        self.field_calls += 1
        return self.field

    def __eq__(self, other: Any) -> bool:
        return self.field == getattr(other, "field", "")

    def __hash__(self) -> int:
        return hash(self.field)


@cache
def present(item: HasComputedField) -> str:
    return f"***--{item.computed_field}--***"


def test_cache_present__call_many_times_with_same_object_wo_custom_eq_method() -> None:
    # Arrange
    item = ObjectWithoutCustomEqMethod(field="test-field")

    # Act
    result = [present(item) for _ in range(3)]

    # Assert
    assert all(presented == "***--test-field--***" for presented in result)
    assert item.field_calls == 1


def test_cache_present__call_many_times_objects_without_eq_method_but_equal() -> None:
    # Arrange
    items = [ObjectWithoutCustomEqMethod(field="test-field") for _ in range(3)]

    # Act
    result = [present(item) for item in items]

    # Assert
    assert all(presented == "***--test-field--***" for presented in result)
    assert all(item.field_calls == 1 for item in items)


def test_cache_present__call_many_times_equal_objects_with_eq_and_hash() -> None:
    # Arrange
    items = [ObjectWithCustomEqMethod(field="test-field") for _ in range(3)]

    # Act
    result = [present(item) for item in items]

    # Assert
    assert all(presented == "***--test-field--***" for presented in result)
    assert items[0].field_calls == 1
    assert all(item.field_calls == 0 for item in items[1:])
