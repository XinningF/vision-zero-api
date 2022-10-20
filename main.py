from fastapi import FastAPI
from routes.crashHistory_route import api_router

app = FastAPI()

app.include_router(api_router)

