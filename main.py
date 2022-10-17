import json
from app.application.login import LoginController, Controller
from fastapi import FastAPI, APIRouter, HTTPException, Request, Response

app = FastAPI()
router = APIRouter()


class Auth:
    async def __call__(self, request: Request):
        authorization = request.headers.get("Authorization")
        if authorization:
            _scheme, token = authorization.split(" ")

        # Token validator

        if not authorization:
            raise HTTPException(
                403,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"token": token}


def adapter(controller: Controller, dependencies=[]):
    async def wrap(request: Request):
        args = {}
        for deps in dependencies:
            d = await deps(request)
            args = {**args, **d}

        body = await request.body()
        body = json.loads(body) if body else {}

        query = dict(request.query_params)
        params = request.path_params

        status, data = await controller.handle({**body, **query, **params, **args})

        return Response(json.dumps(data), status)

    return wrap


router.add_api_route(path="/{id}", methods=["POST"], endpoint=adapter(LoginController(), dependencies=[Auth()]))


app.include_router(router)
