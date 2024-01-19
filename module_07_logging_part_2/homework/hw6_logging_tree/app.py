import logging
from logging import config

from config_dict import dict_config
from utils import string_to_operator
import logging_tree

logging_tree.printout()

logging.config.dictConfig(dict_config)

app_logger = logging.getLogger('app_logger')
app_logger.setLevel(level="DEBUG")


def calc(args):

    with open(file='logging_tree.txt', mode='w', encoding='utf-8') as file:
        file.write(logging_tree.format.build_description())

    # print("Arguments: ", args)
    app_logger.info(msg=f'Arguments: {args}')

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        # print("Error while converting number 1")
        app_logger.error(msg="Error while converting number 1")
        # print(e)
        app_logger.error(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        # print("Error while converting number 2")
        app_logger.error(msg="Error while converting number 2")
        # print(e)
        app_logger.error(e)

    operator_func = string_to_operator(operator)

    try:
        result = operator_func(num_1, num_2)
        # print("Result: ", result)
        app_logger.info(msg=f'Result: {result}')
        # print(f"{num_1} {operator} {num_2} = {result}")
        app_logger.info(msg=f'{num_1} {operator} {num_2} = {result}')
    except Exception as exc:
        app_logger.exception(exc)


if __name__ == '__main__':
    # calc(sys.argv[1:])
    calc('4+3')
