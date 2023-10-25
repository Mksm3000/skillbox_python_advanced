import os
import random
import re
from datetime import datetime, timedelta

from flask import Flask

app = Flask(__name__)

COUNTER_VISITS = 0
CARS_LIST = ['Chevrolet', 'Renault', 'Ford', 'Lada']
CATS_LIST = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
BOOK_LIST = []


def counter_plus():
    global COUNTER_VISITS
    COUNTER_VISITS += 1


def book_to_list():
    global BOOK_LIST
    base_dir = os.path.dirname(os.path.abspath(__file__))
    book_file = os.path.join(base_dir, 'war_and_peace.txt')

    if len(BOOK_LIST) == 0:
        with open(file=book_file, mode='r', encoding='utf-8') as book:
            for line in book:
                line = line.strip('\n')
                pattern = r'[a-zA-Zа-яА-Я]+'
                line_re = ' '.join(re.findall(pattern, line))
                BOOK_LIST.extend(line_re.split(' '))
    return BOOK_LIST


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    data = ', '.join(CARS_LIST)
    return f'Список машин: {data}'


@app.route('/cats')
def cats():
    return f'Случайная порода кошки: {random.choice(CATS_LIST)}'


@app.route('/get_time/now')
def time_now():
    current_time = datetime.now().utcnow()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f'Точное время через час будет: {current_time_after_hour}'


@app.route('/get_random_word')
def random_word():
    return f'Случайное слово из книги "Война и Мир": {random.choice(BOOK_LIST)}'


@app.route('/counter')
def counter():
    counter_plus()
    return f'Я возвращаю число, показывающее, сколько раз открывалась текущая страница - {COUNTER_VISITS}.'


if __name__ == '__main__':
    book_to_list()
    app.run(host='127.0.0.1', port=5555, debug=True)
