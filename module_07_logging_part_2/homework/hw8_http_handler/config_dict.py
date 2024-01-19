import logging
import sys


class ASCIIfilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        if str(record).isascii():
            return True
        else:
            return False


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S"
        }
    },
    "filters": {
        "ascii_filter": {
            "()": ASCIIfilter
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filters": ["ascii_filter"],
            "stream": sys.stdout
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "level": "DEBUG",
            "filename": "calc.log",
            "mode": "a"
        },
        "http_handler": {
            "()": "logging.handlers.HTTPHandler",
            "level": "DEBUG",
            "host": "127.0.0.1:5000",
            "url": "/log",
            "method": "POST"
        },
        "rotated_file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "h",
            "interval": 10,
            "backupCount": 0,
            "encoding": None,
            "delay": False,
            "utc": False,
            "atTime": None,
            "formatter": "simple",
            "level": "INFO",
            "filename": "utils.log"
        }
    },
    "loggers": {
        "app_logger": {
            "level": "DEBUG",
            "handlers": ["console", "file", "http_handler"],
            "propagate": False
         },
        "util_logger": {
            "level": "DEBUG",
            "handlers": ["console", "rotated_file", "http_handler"],
            "propagate": False
        },
    },
}
