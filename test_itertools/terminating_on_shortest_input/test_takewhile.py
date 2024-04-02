from itertools import takewhile


def test_takewhile() -> None:
    # Arrange                        \|/ this dot will be lost
    message = "Greetings from Taganrog. Python is still popular here."
    iterator = iter(message)
    # Act
    result = takewhile(lambda char: char != ".", iterator)

    # Assert
    assert "".join(result) == "Greetings from Taganrog"
    assert "".join(iterator) == " Python is still popular here."
