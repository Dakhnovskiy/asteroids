import logging
import logging.config

from fastapi import FastAPI
from fastapi.routing import Request
from starlette.responses import JSONResponse

from src.api.v1.views.asteroids import asteroids_views
from src.api.v1.views.images import images_views
from src.app.logging_config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

app = FastAPI()


@app.exception_handler(500)
async def on_500(request: Request, exc: Exception):
    logging.exception(exc)
    return JSONResponse(
        status_code=500,
        content={'detail': 'Something went wrong!'},
    )


app.include_router(asteroids_views, prefix='/v1')
app.include_router(images_views, prefix='/v1')
