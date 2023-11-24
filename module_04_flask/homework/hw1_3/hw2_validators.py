"""
Довольно неудобно использовать встроенный валидатор NumberRange
для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры мин и макс — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field, ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if not min <= len(str(field.data)) <= max:
            if min == max:
                raise ValidationError(message=f"{message}. Должно быть {max} цифр.")
            raise ValidationError(message=f"{message}. Должно быть от {min} до {max} цифр.")

    return _number_length


class NumberLength:

    def __init__(self, min: int = 10, max: int = 10):
        self.min = min
        self.max = max

    def __call__(self, form: FlaskForm, field: Field):
        if not self.min <= len(str(field.data)) <= self.max:
            if self.min == self.max:
                raise ValidationError(message=f"Номер телефона должен быть {self.max} цифр.")
            raise ValidationError(message=f"Номер телефона должен быть от {self.min} до {self.max} цифр.")
