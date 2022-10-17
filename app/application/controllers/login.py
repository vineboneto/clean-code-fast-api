from app.core import Controller


class LoginController(Controller):
    async def perform(self, request):
        return 200, {"hello": "vINICIUS"}
