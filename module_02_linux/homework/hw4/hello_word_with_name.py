"""
Реализуйте endpoint /hello-world/<имя>,
который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом,
на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime


app = Flask(__name__)

WEEKDAYS = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы',
            'воскресенья')
GOODS = ('Хорошего', 'Хорошей')


@app.route('/hello-world/<string:username>')
def hello_world(username):
    weekday = datetime.today().weekday()
    nice = GOODS[0]
    if weekday not in (0, 1, 3, 6):
        nice = GOODS[1]
    return f'Привет, {username.title()}. {nice} {WEEKDAYS[weekday]}!'\



if __name__ == '__main__':
    app.run(debug=True)
