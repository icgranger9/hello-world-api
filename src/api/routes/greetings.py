from fastapi import APIRouter

router = APIRouter(prefix="/greetings", tags=["greetings"])

@router.get("/")
async def get_greeting():
    return {"message": "Hello from the greetings route!"}

@router.get("/{name}")
async def get_personalized_greeting(name: str):
    return {"message": f"Hello, {name}!"}