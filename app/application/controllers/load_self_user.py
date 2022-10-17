from app.core import Controller, HTTP, Loader


class LoadSelfUserController(Controller):
    def __init__(self, load_user_by_id: Loader):
        super().__init__()
        self.load_user_by_id = load_user_by_id

    async def perform(self, request):
        user = await self.load_user_by_id.load(request["current_user_id"])

        return HTTP.ok({"id_user": user["id_user"], "username": user["username"], "email": user["email"]})
