import json

from aredis import StrictRedis

from src.app.config import config


redis_client = StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT)


def save_to_redis(key: str, data: dict, expire_time: int) -> None:
    """
    save data to redis
    :param key: key
    :param data: data
    :param expire_time: ttl data
    """
    await redis_client.set(key, json.dumps(data))
    await redis_client.expire(key, expire_time)


def exists_in_redis(key: str) -> bool:
    """
    Check key in redis
    :param key: key
    :return: True/False
    """
    return await redis_client.exists(key)
