from fastapi import FastAPI, APIRouter
from app.application.controllers import AddUserController, LoginController
from app.infra.pg import CheckExistEmailPg, AddUserPg, LoadUserByEmail
from app.infra.crypto import CryptoAdapter
from app.infra.token import JwtAdapter
from app.main.adapter import adapter_controller as adapt
from app.main.middlewares import auth

app = FastAPI()
router = APIRouter()


def login_router():
    controller = LoginController(LoadUserByEmail(), JwtAdapter(), CryptoAdapter())
    return adapt(controller)


def add_user_router():
    controller = AddUserController(CheckExistEmailPg(), AddUserPg(), CryptoAdapter())
    return adapt(controller)


router.add_api_route(path="/users/login", methods=["POST"], endpoint=login_router())
router.add_api_route(path="/users/create", methods=["POST"], endpoint=add_user_router())


app.include_router(router)
