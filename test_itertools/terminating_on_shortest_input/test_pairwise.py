from itertools import pairwise


def test_emtpy() -> None:
    # Act\Assert
    assert list(pairwise([])) == []


def test_fewer_then_2_items() -> None:
    # Act\Assert
    assert list(pairwise([1])) == []


def test_pairwise() -> None:
    # Act\Assert
    assert list(pairwise("ABCD")) == [("A", "B"), ("B", "C"), ("C", "D")]
