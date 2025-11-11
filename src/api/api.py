from fastapi import APIRouter

from api.routes import greetings, health

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(greetings.router)


@api_router.get("/")
async def get_home():
    return {"message": "Hello from the api route!"}