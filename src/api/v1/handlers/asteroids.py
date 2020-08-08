from fastapi import APIRouter

asteroids_handlers = APIRouter()


@asteroids_handlers.post('/asteroids', status_code=201)
async def upload_asteroids():
    return {"message": "asteroid added"}
