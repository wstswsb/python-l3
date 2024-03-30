from dataclasses import dataclass
from functools import singledispatch


@dataclass(frozen=True, slots=True)
class Book:
    title: str
    author: str
    pages: int


@dataclass(frozen=True, slots=True)
class Song:
    name: str
    author: str
    duration_seconds: int


@dataclass(frozen=True, slots=True)
class Picture:
    name: str
    author: str
    year: int


@singledispatch
def build_description(product: Book, price: int) -> str:
    return (
        f"[{price} money] - "
        f"Book \"{product.title}\" "
        f"written by {product.author} "
        f"contains {product.pages} pages."
    )


@build_description.register
def _(product: Song, price: int) -> str:  # type: ignore
    return (
        f"[{price} money] - "
        f"Song \"{product.name}\" "
        f"recorded by {product.author} "
        f"lasting {product.duration_seconds} seconds."
    )


@build_description.register
def _(product: Picture, price: int) -> str:  # type: ignore
    return (
        f"[{price:_} money] - "
        f"Painting \"{product.name}\" "
        f"painted by {product.author} "
        f"in {product.year}."
    )


def test_build_description__book() -> None:
    # Arrange
    book = Book(title="Недоросль", author="Д. И. Фонвизин", pages=256)
    price = 224

    # Act
    result = build_description(book, price)

    # Assert
    expected = (
        '[224 money] - Book "Недоросль" written by Д. И. Фонвизин contains 256 pages.'
    )
    assert result == expected


def test_build_description__song() -> None:
    # Arrange
    song = Song(name="Кто вы?", author="А. Пушной", duration_seconds=126)
    price = 14

    # Act
    result = build_description(song, price)  # type: ignore

    # Assert
    expected = (
        '[14 money] - Song "Кто вы?" recorded by А. Пушной lasting 126 seconds.'
    )
    assert result == expected


def test_build_description__picture() -> None:
    # Arrange
    picture = Picture(name="Девятый вал", author="И. Айвазовский", year=1850)

    # Act
    result = build_description(picture, price=1_000_000)  # type: ignore

    # Assert
    expected = (
        '[1_000_000 money] - '
        'Painting "Девятый вал" '
        'painted by И. Айвазовский '
        'in 1850.'
    )
    assert result == expected
