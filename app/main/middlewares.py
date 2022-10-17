from app.main.adapter import adapter_middleware
from app.application.middlewares import AuthMiddleware


def auth():
    return adapter_middleware(AuthMiddleware())
