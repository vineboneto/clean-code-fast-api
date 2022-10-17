from app.core import Controller, HTTP


class LoginController(Controller):
    async def perform(self, request):
        return HTTP.no_content()

    def get_schema(self):
        return {"name": str, "age": int}
