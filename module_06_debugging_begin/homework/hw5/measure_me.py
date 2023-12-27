"""
Каждый лог содержит в себе метку времени, а значит, правильно организовав логирование,
можно отследить, сколько времени выполняется функция.

Программа, которую вы видите, по умолчанию пишет логи в stdout. Внутри неё есть функция measure_me,
в начале и в конце которой пишется "Enter measure_me" и "Leave measure_me".
Сконфигурируйте логгер, запустите программу, соберите логи и посчитайте среднее время выполнения функции measure_me.
"""
import logging
import random
import subprocess
from typing import List

logger = logging.getLogger(__name__)


def convert_str_to_float(element: str) -> float:
    hour, min, sec = element.split(':')
    sec, millisec = sec[:2], sec[2:]
    return float(hour) * 3600 + float(min) * 60 + float(sec) + float('0.' + millisec)


def convert_list_to_mean(income: list) -> float:
    table = list()
    temp_list = list()

    for element in income:
        element_ = element.split(' - ')
        name = element_[-1]
        if name == 'Enter measure_me':
            temp_list.append(convert_str_to_float(element_[0]))
        else:
            temp_list.append(convert_str_to_float(element_[0]))
            differ = abs(temp_list[0] - temp_list[1])
            table.append(differ)
            temp_list = list()

    return sum(table) / len(table)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG",
                        filemode='w',
                        filename='measure_logger.log',
                        format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                        datefmt='%H:%M:%s')
    for it in range(15):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)

    command = "grep -E '(Enter measure_me|Leave measure_me)' measure_logger.log"
    result = subprocess.run(command, capture_output=True, shell=True)

    data = list(filter(None, result.stdout.decode().split('\n')))
    answer = convert_list_to_mean(data)
    print(f'Среднее время выполнения функции measure_me - {answer} сек')
