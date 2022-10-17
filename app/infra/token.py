from app.core import TokenGenerator
from datetime import datetime, timedelta
from dotenv import dotenv_values
from jose import jwt

env = dotenv_values()


class JwtAdapter(TokenGenerator):
    def __init__(self) -> None:
        TokenGenerator.__init__(self)
        self.jwt = jwt
        self.JWT_SECRET_KEY = env["JWT_SECRET_KEY"]
        self.JWT_REFRESH_SECRET_KEY = env["JWT_REFRESH_SECRET_KEY"]

    async def encode(self, subject: str, secret: str, expires_delta: int = None) -> str:
        exp = datetime.utcnow() + timedelta(minutes=30) if not expires_delta else expires_delta

        to_encode = {"exp": exp, "sub": subject}

        encoded_jwt = self.jwt.encode(to_encode, secret, algorithm=["HS256"])

        return encoded_jwt

    async def decode(self, hashed: str, secret: str):
        digest = self.jwt.decode(hashed, secret, algorithms=["HS256"])

        return digest
