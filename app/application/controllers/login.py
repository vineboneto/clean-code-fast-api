from app.core import Controller


class LoginController(Controller):
    async def perform(self, request):
        print(request)
        return 200, {"hello": "vINICIUS"}
