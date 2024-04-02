from itertools import tee
from typing import Iterator


def test_tee() -> None:
    # Arrange
    gen_calls = 0

    def gen() -> Iterator[int]:
        nonlocal gen_calls
        yield 1
        gen_calls += 1
        yield 2
        gen_calls += 1

    origin_iterator = gen()

    # Act
    iter1, iter2, iter3 = tee(origin_iterator, 3)

    # Assert
    assert list(iter1) == [1, 2]
    assert list(iter2) == [1, 2]
    assert list(iter3) == [1, 2]
    assert gen_calls == 2
