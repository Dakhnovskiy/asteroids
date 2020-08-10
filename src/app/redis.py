import json
from typing import Optional

from aredis import StrictRedis

from src.app.config import config


redis_client = StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)


async def save_to_redis(key: str, data: dict, expire_time: int) -> None:
    """
    save data to redis
    :param key: key
    :param data: data
    :param expire_time: ttl data(seconds)
    """
    await redis_client.set(key, json.dumps(data))
    await redis_client.expire(key, expire_time)


async def exists_in_redis(key: str) -> bool:
    """
    check key in redis
    :param key: key
    :return: True/False
    """
    return await redis_client.exists(key)


async def get_from_redis(key: str) -> Optional[dict]:
    """
    get data by key from redis
    :param key: key
    :return: data
    """
    return json.loads(await redis_client.get(key))
