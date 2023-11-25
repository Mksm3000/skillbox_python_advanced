"""
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

1) email (текст, обязательно для заполнения, валидация формата);
2) phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
3) name (текст, обязательно для заполнения);
4) address (текст, обязательно для заполнения);
5) index (только числа, обязательно для заполнения);
6) comment (текст, необязательно для заполнения).
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange, Length
from module_04_flask.homework.hw1_3.hw2_validators import number_length, NumberLength

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(label="Email: ",
                        validators=[InputRequired("Обязательно для заполнения"),
                                    Email("Некорректный email")])
    # phone = IntegerField(validators=[InputRequired(), NumberLength()])
    phone = IntegerField(validators=[InputRequired(),
                                     number_length(min=9, max=11, message="Номер телефона указан неверно")])
    name = StringField(label="Name: ", validators=[InputRequired("Обязательно для заполнения")])
    address = StringField(label="Address: ", validators=[InputRequired("Обязательно для заполнения")])
    index = IntegerField(label="Index: ", validators=[InputRequired("Обязательно для заполнения")])
    comment = StringField(label="Comment: ")


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone, name, address, index, comment = (
            form.email.data, form.phone.data, form.name.data, form.address.data,
            form.index.data, form.comment.data)

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
