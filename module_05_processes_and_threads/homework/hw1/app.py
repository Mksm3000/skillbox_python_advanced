"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""
import os
import shlex
import subprocess
from typing import List
import signal

from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError

    pids: List[int] = []
    command = f'lsof -i :{port}'

    clear = shlex.split(command)
    # p = subprocess.Popen(clear, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True) не отрабатывает

    # p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    # (out, err) = p.communicate()

    p = subprocess.run(clear, capture_output=True)
    out = p.stdout.decode()

    # with open('out.txt', 'w', encoding='utf-8') as file:
    #     file.write(out)
    #     print('out.txt is created')

    for pid in out.split('\n')[1:-1]:
        num = pid.split(' ')[2]
        print(f'PID {num} on port {port} now')
        pids.append(int(num))

    return pids


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: List[int] = get_pids(port)

    for pid in pids:
        os.kill(pid, signal.SIGKILL)
        # command = f'kill -9 {pid}'
        # clear = shlex.split(command)
        # p = subprocess.run(clear, capture_output=True)
        # # p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        # if p.returncode == 0:
        #     print(f'PID {pid} is dead. Port: {port} is FREE!')


def run(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)
