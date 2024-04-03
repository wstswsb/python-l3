from threading import Thread, current_thread


def test_current_thread() -> None:
    # Act
    result = current_thread()

    # Assert
    assert isinstance(result, Thread)
