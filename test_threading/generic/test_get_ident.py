from threading import get_ident


def test_get_ident() -> None:
    # Act
    result = get_ident()

    # Assert
    assert isinstance(result, int)
    assert result > 0
