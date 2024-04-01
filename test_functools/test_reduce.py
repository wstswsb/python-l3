from dataclasses import dataclass
from functools import reduce
from operator import add
from typing import Literal

_Content = Literal["cinema", "game", "book"]
_Owner = Literal["Author", "Publisher", "Folk art"]


@dataclass(slots=True, frozen=True, match_args=True)
class Slide:
    content: _Content


def define_possible_owners(slide: Slide) -> list[_Owner]:
    match slide:
        case Slide(content="cinema"):
            return ["Publisher"]
        case Slide(content="book"):
            return ["Author", "Folk art"]
        case Slide(content="game"):
            return ["Author"]
        case _:
            return []


def test_define_possible_owners() -> None:
    # Arrange
    slides = (Slide("cinema"), Slide("game"), Slide("book"))

    # Act
    reduce_result = reduce(add, [define_possible_owners(slide) for slide in slides])
    lc_result = [
        possible_owner
        for slide in slides
        for possible_owner in define_possible_owners(slide)
    ]
    # Assert
    assert reduce_result == lc_result == ["Publisher", "Author", "Author", "Folk art"]
