import threading

thread_local = threading.local()
thread_shared = {}
log = []


def target(value: str | None) -> None:
    thread_local.value = value

    with threading.Lock():
        thread_shared["value"] = value
        log.append(value)
    return thread_local.value


def test_local() -> None:
    # Arrange
    target("main-value")
    t1 = threading.Thread(target=target, args=("t1-value",))
    t2 = threading.Thread(target=target, args=("t2-value",))

    # Act
    t1.start()
    t1.join()
    t2.start()
    t2.join()

    # Assert
    assert log == ["main-value", "t1-value", "t2-value"]
    assert thread_local.value == "main-value"
    assert thread_shared["value"] == "t2-value"
