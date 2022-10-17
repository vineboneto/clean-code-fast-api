from app.core import Controller, Middleware
from fastapi import Request, Response, HTTPException
from json import dumps, loads


def adapter_controller(controller: Controller, dependencies=[]):
    async def get_params(request: Request):
        args = {}
        for deps in dependencies:
            d = await deps(request)
            args = {**args, **d}

        body = await request.body()
        body = loads(body) if body else {}

        query = dict(request.query_params)
        params = request.path_params

        return {**query, **params, **args, **body}

    async def wrap(request: Request):
        args = await get_params(request)

        status, data = await controller.handle(args)

        return Response(dumps(data) if data else data, status)

    return wrap


def adapter_middleware(middleware: Middleware):
    async def wrap(request: Request):
        authorization = request.headers.get("Authorization")

        if not authorization:
            raise HTTPException(403, "Missing token")

        _bearer, token = authorization.split(" ")

        status, data = await middleware.handle({"token": token})

        if status in [403, 401]:
            raise HTTPException(status, data["detail"])

        return data

    return wrap
