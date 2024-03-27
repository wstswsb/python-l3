from functools import cached_property

import pytest


class SlotsStructure:
    __slots__ = ("field",)

    def __init__(self, field: str):
        self.field = field

    @cached_property  # Defined for tests. Must raise TypeError
    def computed_field(self) -> str:
        return self.field * 2


class Structure:
    def __init__(self, field: str):
        self.field = field
        self.field_calls = 0

    @cached_property
    def computed_field(self) -> str:
        self.field_calls += 1
        return self.field * 2


def test_cached_property__type_error_when_class_has_slots() -> None:
    # Arrange
    sut = SlotsStructure(field="test-field")

    # Act/Assert
    with pytest.raises(TypeError):
        sut.computed_field  # noqa


def test_cached_property__reassign_value() -> None:
    # Arrange
    sut = Structure(field="test-field")

    # Act\Assert
    origin_value = sut.computed_field
    assert origin_value == "test-field" * 2
    assert sut.field_calls == 1

    sut.computed_field = "new-value"
    assert sut.computed_field == "new-value"

    del sut.computed_field
    assert sut.computed_field == "test-field" * 2
    assert sut.field_calls == 2
