from app.core import Adder, Controller, HTTP, Checker, Hasher
from schema import Regex


class AddUserController(Controller):
    def __init__(self, check_exist_email: Checker, add_user: Adder, generate_hash: Hasher):
        super().__init__()
        self.check_exist_email = check_exist_email
        self.generate_hash = generate_hash
        self.add_user = add_user

    async def perform(self, request):
        exist = await self.check_exist_email.check(request["email"])

        if not exist:
            pass_hash = await self.generate_hash.hasher(request["password"])
            data = await self.add_user.add({**request, "password": pass_hash})

            return HTTP.ok(data)

        return HTTP.conflict("Esse email ja esta sendo utilizado")

    def get_schema(self):
        regex = r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
        return {
            "username": str,
            "password": str,
            "email": Regex(regex),
        }
