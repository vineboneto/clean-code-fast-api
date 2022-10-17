from abc import ABC, abstractmethod
from typing import Any


# Application


class HTTP:
    def ok(data: dict):
        return 200, data

    def no_content():
        return 204, ""

    def bad_request(detail):
        return 400, {"detail": detail}

    def conflict(detail):
        return 400, {"detail": detail}

    def server_error(detail):
        return 500, {"detail": detail}

    def forbidden(detail):
        return 403, {"detail": detail}

    def unauthorized(detail):
        return 401, {"detail": detail}


class Controller:
    async def perform(self, inputs) -> tuple[int, dict]:
        pass

    def get_schema(self):
        pass

    async def handle(self, inputs) -> tuple[int, dict]:
        try:
            error = await self.validate(inputs)
            if error:
                return HTTP.bad_request(str(error))
            return await self.perform(inputs)
        except Exception as e:
            return HTTP.server_error(str(e))

    async def validate(self, inputs) -> bool:
        if self.get_schema():
            from schema import Schema

            try:
                schema = Schema(self.get_schema(), ignore_extra_keys=True)
                schema.validate(inputs)
            except Exception as e:
                return str(e)


class Middleware(ABC):
    @abstractmethod
    async def handle(self, inputs):
        pass


## Infra
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


class Loader(ABC):
    @abstractmethod
    async def load(self, inputs=None):
        pass


class Adder(ABC):
    @abstractmethod
    async def add(self, inputs=None):
        pass


class Checker(ABC):
    @abstractmethod
    async def check(self, inputs=None) -> bool:
        pass
