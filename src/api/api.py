from fastapi import APIRouter

from api.routes import greetings, health

router = APIRouter()
router.include_router(health.router)
router.include_router(greetings.router)


@router.get("/")
async def get_home():
    return {"message": "Hello from the api route!"}