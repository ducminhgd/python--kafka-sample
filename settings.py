import os
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': os.getenv('LOGGING_DISABLE_EXISTING_LOGGERS', 'False') == 'True',
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '%(asctime)s | %(levelname)s | %(process)d | %(thread)d | %(filename)s:%(lineno)d | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': os.getenv('LOGGING_HANDLERS_CONSOLE_LEVEL', 'DEBUG'),
            'formatter': os.getenv('LOGGING_HANDLERS_CONSOLE_FORMATTER', 'verbose')
        },
    },
    'loggers': {
        'main': {
            'level': os.getenv('LOGGING_LOGGERS_MAIN_LEVEL', 'INFO'),
            'handlers': os.getenv('LOGGING_LOGGERS_MAIN_HANDLERS', 'console').split(','),
            'propagate': False
        },
    },
}

logging.config.dictConfig(LOGGING)


KAFKA_BROKERS = os.getenv('KAFKA_BROKERS', '127.0.0.1:9092')
