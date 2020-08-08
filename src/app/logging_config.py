from src.app.config import config


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': (
                '%(levelname)s::%(asctime)s:%(name)s.'
                '%(funcName)s\n%(message)s\n'
            ),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'level': config.LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },
    'loggers': {
        '': {
            'level': config.LOG_LEVEL,
            'handlers': (['console']),
        },
    },
}
