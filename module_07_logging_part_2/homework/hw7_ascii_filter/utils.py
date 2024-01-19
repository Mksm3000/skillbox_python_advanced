import logging
from logging import config
from operator import sub, mul, truediv, add
from typing import Union, Callable

from config_dict import dict_config

logging.config.dictConfig(dict_config)

util_logger = logging.getLogger('util_logger')
util_logger.setLevel(level="DEBUG")

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """

    if not isinstance(value, str):
        # print("wrong operator type", value)
        util_logger.warning(msg=f'wrong operator type: {value}')
        try:
            raise ValueError("wrong operator type")
        except Exception as exc:
            util_logger.exception(exc)

    if value not in OPERATORS:
        # print("wrong operator value", value)
        util_logger.warning(msg=f'wrong operator value: {value}')
        try:
            raise ValueError("wrong operator value")
        except Exception as exc:
            util_logger.exception(exc)

    return OPERATORS[value]
