from pathlib import Path

from src.app.config import config


def make_upload_folder():
    Path(config.UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    make_upload_folder()
