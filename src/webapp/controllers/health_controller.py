from fastapi import APIRouter

health_route = APIRouter()

@health_route.get("/")
async def health_check():
    return {"status": "OK", "message": "'Vozes na Tech' Application is running"}
