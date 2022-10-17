from abc import ABC, abstractmethod
from typing import Any


class TokenGenerator(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    async def encode(self, payload: str, secret: str, expires_time: int = None) -> str:
        pass

    @abstractmethod
    async def decode(self, hashed: str, secret: str) -> Any:
        pass


class Hasher(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    async def hasher(self, payload: str) -> str:
        pass

    @abstractmethod
    async def verify(self, payload: str, hasher: str) -> bool:
        pass
