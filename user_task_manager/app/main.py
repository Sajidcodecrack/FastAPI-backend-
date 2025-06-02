from fastapi import FastAPI
from app.routers.auth_router import auth_router
from app.routers.task_router import task_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(task_router)
