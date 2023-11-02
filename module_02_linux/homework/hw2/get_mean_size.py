"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys
import re


def get_mean_size(ls_output: str) -> float:
    summa = 0
    count = 0
    block = ls_output.split('\n')[1:]
    if len(block) > 1:
        for line in block:
            line = line.strip('\n')
            pattern = r'[\s]+'
            patch = re.sub(pattern=pattern, repl=',', string=line).split(',')
            if len(line) != 0:
                count += 1
                summa += int(patch[4])
        return round((summa/count), 3)
    else:
        return 0.0


if __name__ == '__main__':
    data: str = sys.stdin.read()
    mean_size: float = get_mean_size(data)
    print(f'средний размер файла в каталоге: {mean_size} bytes')
