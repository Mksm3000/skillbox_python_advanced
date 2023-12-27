"""
1. Сконфигурируйте логгер программы из темы 4 так, чтобы он:

* писал логи в файл stderr.txt;
* не писал дату, но писал время в формате HH:MM:SS,
  где HH — часы, MM — минуты, SS — секунды с ведущими нулями.
  Например, 16:00:09;
* выводил логи уровня INFO и выше.

2. К нам пришли сотрудники отдела безопасности и сказали, что, согласно новым стандартам безопасности,
хорошим паролем считается такой пароль, который не содержит в себе слов английского языка,
так что нужно доработать программу из предыдущей задачи.

Напишите функцию is_strong_password, которая принимает на вход пароль в виде строки,
а возвращает булево значение, которое показывает, является ли пароль хорошим по новым стандартам безопасности.
"""

import getpass
import hashlib
import logging
import re

logger = logging.getLogger("password_checker")
ENGLISH = []


def has_english_word(string):
    for word in ENGLISH:
        if re.search(pattern=word, string=string):
            return True
    return False


def has_uppercase(string):
    return bool(re.search('[А-ЯA-Z]', string))


def has_lowercase(string):
    return bool(re.search('[а-яa-z]', string))


def has_special(string):
    return bool(re.search('[!@#$%^&*()-+=_]', string))


def has_num(string):
    return bool(re.search('[0-9]', string))


def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        logger.warning("Вы ввели слишком короткий пароль (меньше 8 символов).")
        return False
    elif has_english_word(password):
        logger.warning("Вы ввели английское слово.")
        return False
    elif not has_special(password):
        logger.warning("Вы ввели пароль без спец.символа.")
        return False
    elif not has_num(password):
        logger.warning("Вы ввели пароль без цифр.")
        return False
    elif not has_lowercase(password):
        logger.warning("Вы ввели пароль без маленькой буквы.")
        return False
    elif not has_uppercase(password):
        logger.warning("Вы ввели пароль без большой буквы.")
        return False

    return True


def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    elif is_strong_password(password):
        logger.warning("Вы ввели слишком слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("utf-8"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        filename='stderr.txt',
                        format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                        datefmt='%H:%M:%S')
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")

    count_number = 0
    correct_input = False
    while not correct_input:
        try:
            count_number: int = int(input('Введите количество попыток (от 2 до 10): '))
            if 2 <= count_number <= 10:
                correct_input = True
        except:
            logger.warning("Вы ввели некорректные данные. Попробуйте еще раз.")

    try_times = count_number
    logger.info(f"У вас есть {try_times} попыток")

    with open(file='words.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            element = line.replace('\n', '')
            ENGLISH.append(element)

    while count_number:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error(f"Пользователь ввёл неправильный пароль {try_times} раз(а)!")
    exit(1)
