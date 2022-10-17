from app.core import Controller, HTTP, TokenGenerator
from dotenv import dotenv_values

env = dotenv_values()


class RefreshTokenController(Controller):
    def __init__(self, token_generator: TokenGenerator):
        self.JWT_SECRET_KEY = env["JWT_SECRET_KEY"]
        self.JWT_REFRESH_SECRET_KEY = env["JWT_REFRESH_SECRET_KEY"]
        self.token_generator = token_generator

    async def perform(self, request):
        try:
            payload = await self.token_generator.decode(request["refresh_token"], self.JWT_REFRESH_SECRET_KEY)

            new_token = await self.token_generator.encode(payload["sub"], self.JWT_SECRET_KEY)

            return HTTP.ok({"token": new_token, "refresh_token": request["refresh_token"]})
        except Exception as e:
            return HTTP.forbidden("refresh token expired")

    def get_schema(self):
        return {"refresh_token": str}
