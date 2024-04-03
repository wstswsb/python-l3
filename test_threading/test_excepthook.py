import threading


def function_with_exception() -> None:
    raise ValueError("Exception inside function")


def test_excepthook__custom_defined() -> None:
    # Arrange
    thread_name = None
    exc_type = None
    exc_value = None

    def custom_excepthook(args: threading.ExceptHookArgs) -> None:
        nonlocal thread_name, exc_value, exc_type
        thread_name = (threading.current_thread().name,)
        exc_type = (args.exc_type,)
        exc_value = args.exc_value

    threading.excepthook = custom_excepthook
    thread = threading.Thread(target=function_with_exception, name="test-thread")

    # Act
    thread.start()
    thread.join()

    # Assert
    assert thread_name == ("test-thread",)
    assert exc_type == (ValueError,)
    assert str(exc_value) == "Exception inside function"
