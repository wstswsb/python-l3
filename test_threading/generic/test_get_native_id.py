from threading import get_native_id


def test_get_native_id() -> None:
    # Act
    result = get_native_id()

    # Assert
    assert isinstance(result, int)
    assert result > 0
