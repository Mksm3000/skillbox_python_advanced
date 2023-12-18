"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""
import shlex
import subprocess
import time

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(label='code', validators=[InputRequired()])
    timeout = IntegerField(label='timeout', validators=[InputRequired(), NumberRange(min=0, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    command = 'prlimit --nproc=1:1 ' + code
    clear = shlex.split(command)

    p = subprocess.Popen(clear, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        outs, errs = p.communicate(timeout=timeout)
        if p.returncode == 0:
            return outs
        else:
            return errs
    except subprocess.TimeoutExpired:
        p.kill()
        outs, errs = p.communicate()
        return f'Исполнение кода "{code}" не уложилось за {timeout} сек.\n{errs}'


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

    if form.validate_on_submit():
        return run_python_code_in_subproccess(form.code.data, form.timeout.data), 200

    return f"Invalid input, {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
