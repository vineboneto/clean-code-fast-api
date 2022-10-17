from app.core import Loader, Middleware, TokenGenerator, HTTP
from dotenv import dotenv_values

env = dotenv_values()


class AuthMiddleware(Middleware):
    def __init__(self, token_validator: TokenGenerator, load_user_by_id: Loader):
        super().__init__()
        self.token_validator = token_validator
        self.load_user_by_id = load_user_by_id
        self.JWT_SECRET_KEY = env["JWT_SECRET_KEY"]

    async def handle(self, inputs):

        try:
            payload = await self.token_validator.decode(inputs["token"], self.JWT_SECRET_KEY)

            user = await self.load_user_by_id.load(int(payload["sub"]))

            if not user:
                return HTTP.forbidden("User not found")

            return HTTP.ok({"current_user_id": user["id_user"]})
        except Exception as e:
            return HTTP.forbidden("token.expired")
