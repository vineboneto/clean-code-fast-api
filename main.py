from fastapi import FastAPI, Depends, APIRouter, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_token_header(x_token: str = Header()):
    print("Token")
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=403, detail="X-Token header invalid")


router = APIRouter(dependencies=[Depends(oauth2_scheme)], responses={404: {"description": "Not found"}})


@router.get("/")
async def read_root(name, last_name):
    return {"Hello": "World"}
