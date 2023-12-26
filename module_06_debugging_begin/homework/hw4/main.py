"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import json
import subprocess
from collections import defaultdict
from typing import Dict


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: Словарь вида {уровень: количество}
    """
    with open(file='skillbox_json_messages.log', mode='r', encoding='utf-8') as file:
        table = defaultdict(int)
        for line in file:
            temp_dict = json.loads(line)
            table[temp_dict.get('level')] += 1

    return dict(table)


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: Час
    """
    with open(file='skillbox_json_messages.log', mode='r', encoding='utf-8') as file:
        table = defaultdict(int)
        for line in file:
            temp_dict = json.loads(line)
            hour = temp_dict.get('time').split(':')[0]
            table[hour] += 1
    table = dict(table)
    return max(table, key=table.get)


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    time_param = '"time": "05:0[0-9]:[0-59]|05:1[0-9]:[0-59]'
    level_param = '"level": "CRITICAL"'
    command = f"grep -E '{level_param}' skillbox_json_messages.log | grep -E '{time_param}'"

    result = subprocess.run(command, capture_output=True, shell=True)
    clear_result = list(filter(None, result.stdout.decode().split('\n')))
    count = len(clear_result)
    return count


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: Количество сообщений
    """
    command = f"grep -c dog skillbox_json_messages.log"

    result = subprocess.run(command, capture_output=True, shell=True)
    count = int(result.stdout.decode())
    return count


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: Слово
    """
    level_param = '"level": "WARNING"'
    command = f"grep -E '{level_param}' skillbox_json_messages.log"

    result = subprocess.run(command, capture_output=True, shell=True)
    result_as_list = result.stdout.decode('utf-8').split('\n')
    clear_result = list(filter(None, result_as_list))

    table = defaultdict(int)

    for element in clear_result:
        temp_dict = json.loads(element)
        message_as_list = str(temp_dict['message']).split(' ')
        for word in message_as_list:
            table[word] += 1
    table = dict(table)
    return max(table, key=table.get)


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
