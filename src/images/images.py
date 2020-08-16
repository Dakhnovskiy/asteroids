import datetime

from src.images.image_files import generate_path, save_file_on_disc
from src.models.images import Image, AsteroidImage


async def save_image(
        image_binary: bytes,
        image_name: str,
        image_datetime: datetime.datetime,
        asteroids_names: list
) -> dict:
    """
    save image
    :param image_binary: image(binary data)
    :param image_name: name of image
    :param image_datetime: datetime of image
    :param asteroids_names: names of asteroids on image
    :return: saved image data
    """
    image_path = await save_image_binary_data(image_binary, image_name)
    image = await save_image_data(image_path, image_datetime, asteroids_names)
    return image


async def save_image_binary_data(image_binary: bytes, image_name: str) -> str:
    """
    save image binary data
    :param image_binary: image(binary data)
    :param image_name: name of image
    :return: path to image binary data
    """
    return await save_image_binary_data_on_disc(image_binary, image_name)


async def save_image_binary_data_on_disc(image_binary: bytes, image_name: str) -> str:
    """
    save image binary data on disk
    :param image_binary: image(binary data)
    :param image_name: name of image
    :return: path of image file
    """
    image_path = generate_path(image_name)
    await save_file_on_disc(image_path, image_binary)
    return image_path


async def save_image_data(image_path: str, image_datetime: datetime.datetime, asteroids_names: list) -> dict:
    """
    save image data
    :param image_path: path of image file
    :param image_datetime: datetime of image
    :param asteroids_names: names of asteroids on image
    :return: image data
    """
    image_id = await Image.create(image_path, image_datetime)
    await AsteroidImage.create_list(image_id, asteroids_names)
    return {
        'id': image_id,
        'image_datetime': image_datetime,
    }


async def get_image_data_by_id(image_id: int) -> dict:
    """
    get image data by image id
    :param image_id: image id
    :return: image data
    """
    image = await Image.get(image_id)
    return image
