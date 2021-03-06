import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Config:
    LOG_LEVEL = os.environ['LOG_LEVEL']

    PG_HOST = os.environ['PG_HOST']
    PG_PORT = os.environ['PG_PORT']
    PG_DB_NAME = os.environ['PG_DB_NAME']
    PG_USER = os.environ['PG_USER']
    PG_PASSWORD = os.environ['PG_PASSWORD']

    REDIS_HOST = os.environ['REDIS_HOST']
    REDIS_PORT = int(os.environ['REDIS_PORT'])

    LOAD_ASTEROIDS_DATA_INTERVAL = int(os.environ['LOAD_ASTEROIDS_DATA_INTERVAL'])
    LOAD_ASTEROIDS_PAGE_CONCURRENCY = int(os.environ['LOAD_ASTEROIDS_PAGE_CONCURRENCY'])
    LOAD_ASTEROID_MAX_PAGES_FOR_LOADING = int(os.environ['LOAD_ASTEROID_MAX_PAGES_FOR_LOADING'])

    API_KEYS_NASA = os.environ['API_KEYS_NASA'].split(',')
    URL_NASA_ASTEROIDS = os.environ['URL_NASA_ASTEROIDS']

    UPLOAD_FOLDER_NAME = os.environ['UPLOAD_FOLDER_NAME']

    SECRET_KEY = os.environ['SECRET_KEY']
    ALGORITHM = os.environ['ALGORITHM']
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ['ACCESS_TOKEN_EXPIRE_MINUTES'])

    @property
    def UPLOAD_FOLDER(self):
        return os.path.join(BASE_PATH, self.UPLOAD_FOLDER_NAME)

    @property
    def PG_DSN(self):
        return f'postgresql://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB_NAME}'


config = Config()
