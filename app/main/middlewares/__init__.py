from app.main.adapters import adapter_middleware
from app.application.middlewares import AuthMiddleware
from app.infra.pg import LoadUserById
from app.infra.token import JwtAdapter


def auth():
    middleware = AuthMiddleware(JwtAdapter(), LoadUserById())
    return adapter_middleware(middleware)
