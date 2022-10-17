import app.application.controllers as controllers
from app.main.adapters import adapter_controller as adapt
from app.main.middlewares import auth
from app.infra.pg import CheckExistEmailPg, AddUserPg, LoadUserByEmail, LoadUserById
from app.infra.crypto import CryptoAdapter
from app.infra.token import JwtAdapter


def login_router():
    controller = controllers.LoginController(LoadUserByEmail(), JwtAdapter(), CryptoAdapter())
    return adapt(controller)


def add_user_router():
    controller = controllers.AddUserController(CheckExistEmailPg(), AddUserPg(), CryptoAdapter())
    return adapt(controller)


def load_self_user_router():
    controller = controllers.LoadSelfUserController(LoadUserById())
    return adapt(controller, dependencies=[auth()])


def generate_refresh_token_router():
    controller = controllers.RefreshTokenController(JwtAdapter())
    return adapt(controller)
