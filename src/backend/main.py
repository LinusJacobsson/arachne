from api.v1 import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router=router)
