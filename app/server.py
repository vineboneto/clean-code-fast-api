from fastapi import FastAPI, APIRouter
from app.application.controllers import LoginController
from app.infra.sql_server import RepositoryTest
from app.main.adapter import adapter_controller as adapt
from app.main.middlewares import auth

app = FastAPI()
router = APIRouter()


def login_router():
    controller = LoginController(RepositoryTest())
    return adapt(controller, dependencies=[auth()])


router.add_api_route(path="/", methods=["POST"], endpoint=login_router())


app.include_router(router)
