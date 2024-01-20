import sys
from typing import Union, Callable
from operator import sub, mul, truediv, add
import logging

util_logger = logging.getLogger('util_logger')
util_logger.setLevel(level="WARNING")

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
