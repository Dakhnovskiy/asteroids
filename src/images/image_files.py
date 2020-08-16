import os
from pathlib import Path
from uuid import uuid4

import aiofiles

from src.app.config import config


def generate_path(file_name: str) -> str:
    """
    generate path for file save
    :param file_name: name of file
    :return: path
    """
    ext = Path(file_name).suffix
    result_file_name = str(uuid4())
    if ext:
        result_file_name = f'{result_file_name}{ext}'

    result_file_path = os.path.join(config.UPLOAD_FOLDER, result_file_name)

    return result_file_path


async def save_file_on_disc(file_path: str, file_binary_data: bytes) -> None:
    """
    save file on disc
    :param file_path: path to save
    :param file_binary_data: file(binary data)
    """
    async with aiofiles.open(file_path, 'wb') as outfile:
        await outfile.write(file_binary_data)
