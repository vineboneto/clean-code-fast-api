from fastapi import FastAPI, APIRouter
from app.application.controllers import LoginController
from app.main.adapter import adapter_controller as adapt
from app.main.middlewares import auth

app = FastAPI()
router = APIRouter()

router.add_api_route(path="/", methods=["POST"], endpoint=adapt(LoginController(), dependencies=[auth()]))

app.include_router(router)
