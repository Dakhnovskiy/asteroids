from fastapi import APIRouter

asteroids_views = APIRouter()


@asteroids_views.post('/asteroids', status_code=201)
async def upload_asteroids():
    return {"message": "asteroid added"}


@asteroids_views.get('/asteroids', status_code=201)
async def get_asteroid():
    return {"message": "asteroid added"}
