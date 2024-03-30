import time
from functools import wraps
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def timeit_wo_wraps(func):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"{func.__name__} executed for {round(execution_time, 2)} seconds")
        return result

    return wrapper


def timeit_with_wraps(func):  # type: ignore
    @wraps(func)
    def wrapper(*args, **kwargs):  # type: ignore
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"{func.__name__} executed for {round(execution_time, 2)} seconds")
        return result

    return wrapper


def test_timeit__without_and_with_wraps() -> None:
    # Arrange
    def foo(number: int) -> None:
        pass

    foo.__module__ = "test-module"
    foo.__name__ = "test-name"
    foo.__qualname__ = "test-qualname"
    foo.__doc__ = "test-doc"
    foo.__annotations__ = {"number": int}

    # Act
    with_wraps = timeit_with_wraps(foo)  # type: ignore
    without_wraps = timeit_wo_wraps(foo)  # type: ignore

    # Assert
    assert with_wraps.__module__ == foo.__module__
    assert with_wraps.__name__ == foo.__name__
    assert with_wraps.__qualname__ == foo.__qualname__
    assert with_wraps.__doc__ == foo.__doc__
    assert with_wraps.__annotations__ == foo.__annotations__

    assert without_wraps.__module__ != foo.__module__
    assert without_wraps.__name__ != foo.__name__
    assert without_wraps.__qualname__ != foo.__qualname__
    assert without_wraps.__doc__ != foo.__doc__
    assert without_wraps.__annotations__ != foo.__annotations__
