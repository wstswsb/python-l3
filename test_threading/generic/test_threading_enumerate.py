import threading


def test_enumerate__one_running_and_one_joined() -> None:
    # Arrange
    t1_event = threading.Event()
    t2_event = threading.Event()

    # Act
    t1 = threading.Thread(target=lambda: t1_event.wait())
    t2 = threading.Thread(target=lambda: t2_event.wait())
    t1.start()
    t2.start()

    t1_event.set()
    t1.join()

    result = threading.enumerate()

    t2_event.set()
    t2.join()

    # Assert
    assert isinstance(result, list)
    assert len(result) == 2  # main and t2
    assert t2 in result
    assert threading.current_thread() in result
