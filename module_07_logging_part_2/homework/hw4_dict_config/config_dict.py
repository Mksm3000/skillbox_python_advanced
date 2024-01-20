import logging
import sys

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": sys.stdout
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "level": "DEBUG",
            "filename": "calc.log",
            "mode": "a"
        }
    },
    "loggers": {
        "app_logger": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False
         },
        "util_logger": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False
        },
    },
}
