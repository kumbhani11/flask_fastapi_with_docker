from fastapi import FastAPI
from backend.routers import post_api

app = FastAPI()

app.include_router(post_api.router)
