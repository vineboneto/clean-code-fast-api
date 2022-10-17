from app.core import Controller, HTTP, Loader


class LoginController(Controller):
    def __init__(self, load_clientes_repo: Loader) -> None:
        super().__init__()
        self.load_clientes_repo = load_clientes_repo

    async def perform(self, request):
        data = await self.load_clientes_repo.load(request)

        return HTTP.ok(data)

    def get_schema(self):
        return {"name": str, "age": int}
