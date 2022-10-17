from app.core import Hasher
from passlib.context import CryptContext


class CryptoAdapter(Hasher):
    def __init__(self) -> None:
        self.crypto = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def hasher(self, payload: str) -> str:
        return self.crypto.hash(payload)

    async def verify(self, payload: str, hasher: str) -> bool:
        return self.crypto.verify(payload, hasher)
