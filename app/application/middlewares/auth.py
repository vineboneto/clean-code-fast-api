from app.core import Middleware


class AuthMiddleware(Middleware):
    async def handle(self, inputs):
        return 200, {"id_usuario": 1}
