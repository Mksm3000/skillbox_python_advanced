"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:
/ps?arg=a&arg=u&arg=x
"""

from flask import Flask, request, url_for
import shlex
import subprocess

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:

    args: list[str] = request.args.getlist('arg')
    url = url_for('ps').split('/')[1]

    clean_url = shlex.quote(url)
    clean_args = shlex.quote(''.join(args))

    result = subprocess.check_output([clean_url, clean_args]).decode('utf-8')

    return f'<pre>{result}</pre>'


if __name__ == "__main__":
    app.run(debug=True)
