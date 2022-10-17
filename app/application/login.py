class Controller:
    async def perform(self, inputs):
        pass

    async def handle(self, inputs):
        return await self.perform(inputs)


class LoginController(Controller):
    async def perform(self, request):
        return 200, {"hello": "vINICIUS"}
