import asyncio
import logging
import logging.config

from src.app.config import config
from src.app.logging_config import LOGGING_CONFIG
from src.asteroids_data.asteroids_data import load_asteroids_data


logging.config.dictConfig(LOGGING_CONFIG)


async def worker_load_asteroids_data():
    """
    Asteroids data loader
    """
    while True:
        try:
            logging.info('start loading asteroids data')
            await load_asteroids_data()
        except Exception as exc:
            logging.exception(exc)

        logging.info('finish loading asteroids data')
        await asyncio.sleep(config.LOAD_ASTEROIDS_DATA_INTERVAL)


if __name__ == '__main__':
    asyncio.run(worker_load_asteroids_data())
