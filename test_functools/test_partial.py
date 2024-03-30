from functools import partial
from typing import Literal

import pytest


def __present_greetings(surname: str, role: Literal["Doctor", "Nurse"]) -> str:
    if role == "Nurse":
        return f"Hello, Nurse {surname}."

    if surname in {"House", "Cameron", "Foreman", "Chase"}:
        return f"Hello, Dr. {surname} from Diagnostics."
    if role == "Doctor":
        return f"Hello, Dr. {surname}."


doctor_greetings = partial(__present_greetings, role="Doctor")
nurse_greetings = partial(__present_greetings, role="Nurse")
house_greetings = partial(__present_greetings, "House", "Doctor")


@pytest.mark.parametrize(
    ("surname", "expected_result"),
    [
        ("House", "Hello, Dr. House from Diagnostics."),
        ("Cameron", "Hello, Dr. Cameron from Diagnostics."),
        ("Foreman", "Hello, Dr. Foreman from Diagnostics."),
        ("Chase", "Hello, Dr. Chase from Diagnostics.")
    ]
)
def test_doctor_greetings__diagnostics_team(surname: str, expected_result: str) -> None:
    # Act
    partial_result = doctor_greetings(surname)
    origin_result = __present_greetings(surname, role="Doctor")

    # Assert
    assert partial_result == origin_result == expected_result


def test_doctor_greetings__generic_case() -> None:
    # Arrange
    surname = "Wilson"

    # Act
    partial_result = doctor_greetings(surname)
    origin_result = __present_greetings(surname, role="Doctor")

    # Assert
    assert partial_result == origin_result == "Hello, Dr. Wilson."


def test_nurse_greetings__generic_case() -> None:
    # Arrange
    surname = "Character"

    # Act
    partial_result = nurse_greetings(surname)
    origin_result = __present_greetings(surname, role="Nurse")

    # Assert
    assert partial_result == origin_result == "Hello, Nurse Character."


def test_house_greetings() -> None:
    # Act
    partial_result = house_greetings()
    origin_result = __present_greetings("House", "Doctor")

    # Assert
    assert partial_result == origin_result == "Hello, Dr. House from Diagnostics."
