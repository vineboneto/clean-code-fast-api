import app.main.routers as routers
from fastapi import FastAPI


app = FastAPI()


app.include_router(routers.user_routers())
