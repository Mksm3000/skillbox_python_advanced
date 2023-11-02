import math
import re

"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB")
    integer_power = int(math.floor(math.log(size_bytes, 1024)))
    powered_number = math.pow(1024, integer_power)
    size = round(size_bytes / powered_number, 3)
    return f'{size} {size_name[integer_power]}'


def get_summary_rss(ps_output_file_path: str) -> str:
    summa = 0
    with open(file=ps_output_file_path, mode='r', encoding='utf-8') as output_file:
        lines = output_file.readlines()[1:]
        for line in lines:
            line = line.strip('\n')
            pattern = r'[\s]+'
            patch = re.sub(pattern=pattern, repl=',', string=line).split(',')
            summa += int(patch[5])
    return convert_size(summa)


if __name__ == '__main__':
    path: str = 'output_file.txt'
    summary_rss: str = get_summary_rss(path)
    print(f'суммарный объём потребляемой памяти: {summary_rss}')
