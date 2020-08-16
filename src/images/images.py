import datetime

from src.images.image_files import generate_path, save_file_on_disc


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

    return {
        'image_datetime': image_datetime,
        'link': ''
    }


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
    :return: path to image file
    """
    image_path = generate_path(image_name)
    await save_file_on_disc(image_path, image_binary)
    return image_path


async def save_image_data(image_path, image_datetime, asteroids_names):
    pass
