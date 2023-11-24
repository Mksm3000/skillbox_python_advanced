import unittest

from module_04_flask.materials.flask_wtform import app


class TestFlaskWTForm(unittest.TestCase):
    @classmethod
    def setUp(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        cls.app = app.test_client()

    def test_registration(self):
        self.base_url = "/registration"

        test_data = {'email': 'mail@mail.com',
                     'phone': '9991112233',
                     'name': 'Petrov Al.F.',
                     'address': 'Maldives',
                     'index': '101202',
                     'comment': "it's ok"}

        response = self.app.post(self.base_url, data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('Неверно указан номер телефона', response.text)
        self.assertIn('Неверно указано имя', response.text)
