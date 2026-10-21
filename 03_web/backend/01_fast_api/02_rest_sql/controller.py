from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def get():
    return {"ping": "pong"}