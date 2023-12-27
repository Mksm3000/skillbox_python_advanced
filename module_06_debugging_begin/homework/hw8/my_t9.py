"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""
import re
from typing import List

KEYBOARD = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }


# 22736368
def my_t9(input_numbers: str) -> List[str]:
    result = []

    with open(file='words.txt', mode='r', encoding='utf-8') as file:
        pattern = ''
        for num in range(len(input_numbers)):
            digit = input_numbers[num]
            block = ''
            for letter in KEYBOARD[digit]:
                block += letter
            pattern += '[' + block + ']'

        for line in file:
            line = line.strip('\n')
            if re.match(pattern=pattern, string=line) and len(line) == len(input_numbers):
                result.append(line)

    return result


if __name__ == '__main__':
    numbers: str = input('Введите номера клавиш, например "22736368": ')
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
