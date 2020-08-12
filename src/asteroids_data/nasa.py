import httpx
from starlette import status

from src.app.config import config


async def get_asteroids_data_from_nasa_by_page(number_of_page: int) -> dict:
    """
    get data about asteroids from NASA API on one page
    :param number_of_page: number of page
    """

    async with httpx.AsyncClient(verify=False) as client:
        for api_key in config.API_KEYS_NASA:
            resp = await client.get(
                url=config.URL_NASA_ASTEROIDS,
                params={'page': number_of_page, 'api_key': api_key}
            )
            if resp.status_code != status.HTTP_429_TOO_MANY_REQUESTS:
                break
    resp.raise_for_status()
    return resp.json()
