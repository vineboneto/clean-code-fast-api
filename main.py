from fastapi import FastAPI, Depends, APIRouter, HTTPException, Request


app = FastAPI()


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
        return token


router = APIRouter()


@router.get("/")
async def read_root(token=Depends(Auth())):
    print("Depois aqui")
    print("Token", token)
    return {"Hello": "World"}


app.include_router(router)
