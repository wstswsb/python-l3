from functools import lru_cache


@lru_cache
def fib(number: int) -> int:
    if number <= 1:
        return number
    return fib(number - 1) + fib(number - 2)


def test_lru_cache__check_cache_parameters_default() -> None:
    # Act
    result = fib.cache_parameters()

    # Assert
    assert result == {"maxsize": 128, "typed": False}


def test_lru_cache__check_cache_info() -> None:
    """https://recursion.vercel.app/"""
    # На этом сайте можно установить Memoization для fibonacci
    # И увидеть hits, misses (hits - закрашены черным)

    # Arrange
    fib(5)

    # Act
    result = fib.cache_info()

    # Assert

    assert result.hits == 3
    assert result.misses == 6
    assert result.maxsize == 128
    assert result.currsize == 6


def test_lru_cache__check_cache_clear() -> None:
    # Arrange
    fib(5)

    # Act
    fib.cache_clear()

    # Assert
    cache_info = fib.cache_info()
    assert cache_info.hits == 0
    assert cache_info.misses == 0
    assert cache_info.maxsize == 128
    assert cache_info.currsize == 0


def test_lru_cache__typed_true() -> None:
    # Arrange
    call_count = 0

    @lru_cache(typed=True)
    def mul(a: float, b: float) -> float:
        nonlocal call_count
        call_count += 1
        return float(a * b)

    # Act
    mul(1, 2)
    mul(1.0, 2.0)

    # Assert
    assert call_count == 2


def test_lru_cache__typed_false() -> None:
    # Arrange
    call_count = 0

    @lru_cache(typed=False)
    def mul(a: float, b: float) -> float:
        nonlocal call_count
        call_count += 1
        return float(a * b)

    # Act
    mul(1, 2)
    mul(1.0, 2.0)

    # Assert
    assert call_count == 1
