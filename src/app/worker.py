import asyncio
import logging

from src.app.config import config
from src.asteroids_data.asteroids_data import load_asteroids_data


async def worker_load_asteroids_data():
    """
    Asteroids data loader
    """
    while True:
        try:
            await load_asteroids_data()
        except Exception as exc:
            logging.exception(exc)

        await asyncio.sleep(config.LOAD_ASTEROIDS_DATA_INTERVAL)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(worker_load_asteroids_data())
    loop.run_forever()
