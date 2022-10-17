from app.core import Controller, HTTP, Hasher, Loader, TokenGenerator
from datetime import datetime, timedelta
from dotenv import dotenv_values

env = dotenv_values()


class LoginController(Controller):
    def __init__(self, load_user_by_email: Loader, token_generator: TokenGenerator, validator_hash: Hasher):
        super().__init__()
        self.JWT_SECRET_KEY = env["JWT_SECRET_KEY"]
        self.JWT_REFRESH_SECRET_KEY = env["JWT_REFRESH_SECRET_KEY"]
        self.load_user_by_email = load_user_by_email
        self.token_generator = token_generator
        self.validator_hash = validator_hash

    async def perform(self, request):
        data = await self.load_user_by_email.load(request["email"])

        if data:
            is_valid_pass = await self.validator_hash.verify(request["password"], data["password"])
            if is_valid_pass:
                token = await self.token_generator.encode(data["id_user"], self.JWT_SECRET_KEY)
                refresh_token = await self.token_generator.encode(
                    data["id_user"], self.JWT_REFRESH_SECRET_KEY, datetime.utcnow() + timedelta(days=1)
                )

                return HTTP.ok({"token": token, "refresh_token": refresh_token})

        return HTTP.unauthorized("Email ou senha invalido")

    def get_schema(self):
        return {"email": str, "password": str}
