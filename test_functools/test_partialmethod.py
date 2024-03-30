from dataclasses import dataclass
from functools import partialmethod
from typing import Literal, Self

_Status = Literal["todo", "success", "fail"]


@dataclass(slots=True)
class Task:
    name: str
    status: _Status

    @classmethod
    def new(cls, name: str) -> Self:
        return cls(name, "todo")

    def set_status(self, status: _Status) -> None:
        self.status = status

    fail = partialmethod(set_status, "fail")
    success = partialmethod(set_status, "success")


def test_task__new() -> None:
    # Act
    task = Task.new("test")

    # Assert
    assert task.status == "todo"
    assert task.name == "test"


def test_task__fail() -> None:
    # Arrange
    task = Task.new("learn functools")

    # Act
    task.fail()

    # Assert
    assert task.status == "fail"


def test_task__success() -> None:
    # Arrange
    task = Task.new("learn functools")

    # Act
    task.success()

    # Assert
    assert task.status == "success"
