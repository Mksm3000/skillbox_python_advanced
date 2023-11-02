"""
Реализуйте приложение для учёта финансов, умеющее запоминать,
сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD,
где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

import time
from icecream import ic
from flask import Flask

app = Flask(__name__)

STORAGE = {'2021': {'12': 200},
           '2022': {'02': 100500},
           '2023': {'09': 70,
                    '10': 195,
                    '11': 205}
           }


def check_date(input_date: str):
    """
    Проверка даты на корректность.
    :param input_date: Дата в формате YYYYMMDD:str
    :return: Bool
    """
    try:
        valid_date = time.strptime(input_date, '%Y%m%d')
        if valid_date:
            return True
    except:
        return False


def add_in(slovar: dict, date: str, summa: int):
    """
    Добавление суммы трат в словарь с учётом года, месяца.
    :param slovar: Dict проверка существования словаря, года и месяца
    :param date: Str дата траты
    :param summa: Int сумма траты
    :return: None
    """
    year = date[:4]
    month = date[4:6]
    if slovar.get(year):
        if slovar[year].get(month):
            slovar[year][month] += summa
        else:
            slovar[year][month] = summa
    else:
        slovar[year] = {}
        slovar[year][month] = summa


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    """
    Сохранение информации о совершённой в рублях трате за какой-то день
    """
    message = ''
    if check_date(date):
        if number > 0:
            add_in(STORAGE, date, number)
            # ic(STORAGE)
            year = date[:4]
            month = date[4:6]
            day = date[6:]
            message = f'Дата: {year}-{month}-{day}. Расходы {number} успешно добавлены.'
        else:
            message = 'Расходы - это число, больше нуля'
    else:
        message = ('Дата введена неверно, попробуйте ещё раз!\n'
                   'Данные необходимо вводить в формате YYYYMMDD, где\n'
                   'YYYY — год,\n'
                   'MM — месяц (от 01 до 12),\n'
                   'DD — число (от 01 до 31, с учётом месяца, конечно же).\n')
    return message


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    """
    Получение суммарных трат за указанный год
    """
    global STORAGE
    if STORAGE.get(str(year)):
        money = 0
        for value in STORAGE[str(year)].values():
            # ic(value)
            money += value
        message = f'Суммарные траты за {year} год: {money}'
    else:
        message = f'{year} года в данных не существует!\nПопробуйте указать другой год.'
    return message


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    """
    Получение суммарных трат за указанные год и месяц.
    """
    global STORAGE
    if STORAGE.get(str(year)):
        money = 0

        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)

        if STORAGE[str(year)].get(month):
            value = STORAGE[str(year)][month]
            money += value
            message = f'Суммарные траты за {year} год в {month} месяце: {money}'
        else:
            message = (f'Для {year} года {month} месяца в данных не существует!\n'
                       f'Попробуйте указать другой месяц.')
    else:
        message = f'{year} года в данных не существует!\nПопробуйте указать другой год.'
    return message


if __name__ == "__main__":
    app.run(debug=True)
