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
            "handlers": ["console", "file"],
            "propagate": False
         },
        "util_logger": {
            "level": "DEBUG",
            "handlers": ["console", "rotated_file"],
            "propagate": False
        },
    },
}
