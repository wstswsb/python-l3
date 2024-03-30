from functools import singledispatchmethod
from typing import Self


class PositionContainer:
    def __init__(self, value: int):
        self.value = value

    @singledispatchmethod
    @classmethod
    def new(cls, value: int) -> Self:
        cls.__check_positive(value)
        return cls(value)

    @new.register
    @classmethod
    def _(cls, value: float) -> Self:
        rounded_value = round(value)
        cls.__check_positive(rounded_value)
        return cls(rounded_value)

    @new.register
    @classmethod
    def _(cls, value: str) -> Self:
        converted_value = float(value)
        return cls.new(converted_value)

    @staticmethod
    def __check_positive(value: int) -> None:
        if value < 0:
            raise ValueError(f"position cannot be negative: {value=}")


def test_position_container__from_int() -> None:
    container = PositionContainer.new(12)

    assert container.value == 12


def test_position_container__from_float() -> None:
    container = PositionContainer.new(1.2)

    assert container.value == 1


def test_position_container__from_str() -> None:
    container = PositionContainer.new("1.6")

    assert container.value == 2
