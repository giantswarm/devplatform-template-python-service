from enum import Enum
from abc import ABC, abstractmethod


class DataStore(Enum):
    Memory = 1


class Album:
    ID: int
    Title: str
    Artist: str
    Price: float

    def __init__(self, aid: int, title: str, artist: str, price: float):
        self.ID = aid
        self.Title = title
        self.Artist = artist
        self.Price = price


class AlbumStore(ABC):
    @abstractmethod
    def add(self, album: Album) -> int: ...
    @abstractmethod
    def get(self, aid: int) -> Album: ...

    @abstractmethod
    def list(self) -> list[Album]: ...

    @abstractmethod
    def update(self, album: Album): ...

    @abstractmethod
    def remove(self, aid: int): ...


class AlbumNotFound(Exception):
    pass


class InMemoryStore(AlbumStore):
    def __init__(self):
        self._albums = {
            1: Album(1, "All that you can't leave behind", "U2", 56.99),
            2: Album(2, "A night at the opera", "Queen", 17.99),
        }

    def get(self, aid: int) -> Album:
        if aid not in self._albums:
            raise AlbumNotFound()
        return self._albums[aid]

    def list(self) -> list[Album]:
        return list(self._albums.values())

    def update(self, album: Album):
        if album.ID not in self._albums:
            raise AlbumNotFound()
        self._albums[album.ID] = album

    def remove(self, aid: int):
        if aid not in self._albums:
            raise AlbumNotFound()
        self._albums.pop(aid)

    def add(self, album: Album) -> int:
        aid = len(self._albums) + 1
        album.ID = aid
        self._albums[aid] = album
        return aid
