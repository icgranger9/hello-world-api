from fastapi import FastAPI

from src.api import api

API_TITLE = "Hello World API"
API_PREFIX = "/api"

app = FastAPI(title=API_TITLE, openapi_url=f"{API_PREFIX}/openapi.json")

app.include_router(api.router, prefix=API_PREFIX)

@app.get("/")
async def get_home():
    return {"message": "Hello from the app route!"}