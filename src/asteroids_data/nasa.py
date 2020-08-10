import httpx

from src.app.config import config

client = httpx.AsyncClient(
    verify=False,
)


async def get_asteroids_data_from_nasa_by_page(number_of_page: int) -> dict:
    """
    get data about asteroids from NASA API on one page
    :param number_of_page: number of page
    """

    async with client:
        resp = await client.get(
            url=config.URL_NASA_ASTEROIDS,
            params={'page': number_of_page, 'api_key': config.API_KEY_NASA}
        )
    resp.raise_for_status()
    return resp.json()
