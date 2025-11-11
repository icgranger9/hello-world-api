
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/")
async def get_health_check():
    # A simple health check endpoint
    return {"status": "healthy"}
