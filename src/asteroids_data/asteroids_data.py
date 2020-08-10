import asyncio
import logging
from typing import Optional

from src.app import redis
from src.app.config import config
from src.asteroids_data.hash import get_hash
from src.asteroids_data.nasa import get_asteroids_data_from_nasa_by_page


async def load_asteroids_data() -> None:
    """
    load data about asteroids
    """
    count_asteroids_pages = await get_count_asteroids_pages()
    logging.info(f'Count of asteroids pages = {count_asteroids_pages}')
    sem = asyncio.Semaphore(config.LOAD_ASTEROIDS_PAGE_CONCURRENCY)
    await asyncio.gather(*[load_asteroids_data_by_page(sem, page + 1) for page in range(count_asteroids_pages)])


async def get_count_asteroids_pages() -> int:
    """
    get count asteroids pages
    """
    asteroids_data = await get_asteroids_data_from_nasa_by_page(1)
    return asteroids_data['page']['total_pages']


async def get_asteroids_data_by_page(number_of_page: int) -> list:
    """
    get data about asteroids on one page
    :param number_of_page: number of page
    """
    asteroids_data = await get_asteroids_data_from_nasa_by_page(number_of_page)
    return asteroids_data['near_earth_objects']


async def save_asteroids_data_to_storage(asteroids_data: list) -> None:
    """
    save data about asteroids to storage
    :param asteroids_data: list of asteroids data
    """
    await asyncio.gather(*[
        redis.save_to_redis(
            key=get_hash(data['name']),
            data=data,
            expire_time=config.LOAD_ASTEROIDS_DATA_INTERVAL + 60
        ) for data in asteroids_data if data.get('name')
    ])


async def get_asteroid_data_from_storage_by_name(asteroid_name: str) -> Optional[dict]:
    """
    get asteroid data by name from storage
    :param asteroid_name: asteroid name
    :return:
    """
    return await redis.get_from_redis(get_hash(asteroid_name))


async def exists_asteroid_data_by_name(asteroid_name: str) -> bool:
    """
    check asteroid name in storage
    :param asteroid_name: asteroid name
    :return: result of checking (True/False)
    """
    return await redis.exists_in_redis(get_hash(asteroid_name))


async def load_asteroids_data_by_page(semaphore: asyncio.Semaphore, number_of_page: int) -> None:
    """
    get data about asteroids by number of page and save to storage
    :param semaphore: semaphore object
    :param number_of_page: number of page
    """
    async with semaphore:
        asteroids_data = await get_asteroids_data_by_page(number_of_page)
        await save_asteroids_data_to_storage(asteroids_data)
        logging.info(f'page {number_of_page} is loaded')
