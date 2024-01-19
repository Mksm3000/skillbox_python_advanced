import logging
import sys


class LevelFileHandler(logging.Handler):
    
    def __init__(self, filename='', mode='a'):
        super().__init__()
        self.filename = filename
        self.mode = mode

    def emit(self, record:logging.LogRecord):
        msg = self.format(record)
        with open(self.filename + record.levelname + '.log', mode=self.mode) as log:
            log.write(msg + '\n')

# Добавьте handler, который будет писать сообщения разных уровней в соответствующие файлы.
# Например, сообщения уровня debug попадут в файл calc_debug.log,
# а уровня error — в calc_error.log.


def get_logger(name):
    logger = logging.getLogger(name=name)

    formatter = logging.Formatter(fmt='%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
                                  datefmt='%d-%m-%Y %H:%M:%S')

    custom_handler = LevelFileHandler('calc_')
    custom_handler.setFormatter(formatter)

    logger.addHandler(custom_handler)

    return logger

