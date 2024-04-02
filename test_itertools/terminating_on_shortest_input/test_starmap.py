from itertools import starmap
from unittest.mock import Mock, call


def test_starmap() -> None:
    # Arrange
    args = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    )
    callable_mock = Mock(side_effect=("call_1", "call_2", "call_3"))

    # Act
    result = list(starmap(callable_mock, args))

    # Assert
    assert result == ["call_1", "call_2", "call_3"]
    callable_mock.assert_has_calls(
        calls=[
            call(1, 2, 3),
            call(4, 5, 6),
            call(7, 8, 9),
        ]
    )
