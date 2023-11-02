"""
Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра:
SIZE (int) и RELATIVE_PATH —
и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.
В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах,
а во второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

docs/simple.txt
homework/simple.txt


/preview/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/preview/100/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
"""

from flask import Flask
import os
from pprint import pprint

app = Flask(__name__)


@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    abs_path = os.path.abspath(os.path.join(parent_dir, relative_path))

    with open(abs_path, 'r', encoding='utf-8') as file:
        result_size = len(file.read())
        if result_size > size:
            result_size = size

    with open(abs_path, 'r', encoding='utf-8') as file:
        result_text = file.read(size)

    return f'<b>{abs_path}</b> {result_size} <br> {result_text}'


if __name__ == "__main__":
    app.run(debug=True)
