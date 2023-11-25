"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

from flask import Flask
# import os
import shlex, subprocess

app = Flask(__name__)
# UPTIME = os.popen(cmd='uptime -p').read()


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    command_str = f"uptime -p"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True).stdout.decode('utf-8')
    return f"Current uptime is {result}"


if __name__ == '__main__':
    app.run(debug=True)
