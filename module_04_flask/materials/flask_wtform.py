from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
import re
from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[InputRequired()])
    family_name = StringField()
    ticket = IntegerField()
    address = StringField(validators=[InputRequired()])
    index = IntegerField()
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        form_dict = {
            "email": form.email.data,
            "phone": form.phone.data,
            "name": form.name.data,
            "address": form.address.data,
            "index": form.index.data,
            "comment": form.comment.data
        }

        for key, value in form_dict.items():
            if not value:
                return f'Не указан {key}', 400

            if not isinstance(form.phone.data, int) or len(str(form.phone.data)) != 10:
                return f'Неверно указан номер телефона', 400

            pattern = r'[A-Za-zА-Яа-я]+[ ][A-Za-zА-Яа-я]{1}[.][ ]?[A-Za-zА-Яа-я]{1}[.]'
            if not re.match(pattern, form.name.data):
                return f'Неверно указано имя', 400

        return f"Successfully registered user '{form.email.data}' with phone +7{form.phone.data}"

    return f"Invalid input, {form.errors}", 400


@app.route("/lucky", methods=["POST"])
def lucky():
    form = RegistrationForm()

    if form.validate_on_submit():
        form_dict = {
            "name": form.name.data,
            "family_name": form.family_name.data,
            "ticket": form.ticket.data
        }

        for key, value in form_dict.items():
            if not value:
                return f'Не указан {key}', 400

        numbers = str(form.ticket.data)
        if len(numbers) != 6 or numbers.startswith('0'):
            return f'Неверно указан номер билета', 400

        if sum(map(int, numbers[:3])) == sum(map(int, numbers[3:])):
            return f"Поздравляем вас, {form.name.data} {form.family_name.data}", 200
        else:
            return f"Неудача. Попробуйте ещё раз!", 400

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
