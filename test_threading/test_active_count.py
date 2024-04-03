from threading import Thread, active_count
from time import sleep


def test_active_count__only_main_thread() -> None:
    assert active_count() == 1


def test_active_count__new_thread_spawned() -> None:
    # Arrange
    thread = Thread(target=sleep, args=(0.01,))
    thread.start()

    # Act
    result_start = active_count()
    thread.join()
    result_joined = active_count()

    # assert
    assert result_start == 2
    assert result_joined == 1
