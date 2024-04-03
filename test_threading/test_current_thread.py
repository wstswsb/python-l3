from threading import current_thread, Thread


def test_current_thread():
    # Act
    result = current_thread()

    # Assert
    assert isinstance(result, Thread)
