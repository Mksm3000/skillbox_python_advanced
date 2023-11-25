import unittest

from module_04_flask.homework.hw1_3.hw1_registration import app, RegistrationForm


class TestRegistration(unittest.TestCase):
    @classmethod
    def setUp(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        cls.base_url = '/registration'
        cls.app = app.test_client()

        cls.data_ok = {'email': 'mail@mail.com',
                       'phone': '9991112233',
                       'name': 'Petrov A. F.',
                       'address': 'Maldives',
                       'index': '101202',
                       'comment': "it's ok"}

        cls.data_not_ok = {'email': 'mail-megamail.com',
                           'phone': '0a91112233',
                           'name': '',
                           'address': '',
                           'index': '10L202',
                           'comment': "it's n00t ok"}

    def test_email_correct(self):
        response = self.app.post(self.base_url, data=self.data_ok)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfully registered", response.text)

    def test_email_incorrect(self):
        response = self.app.post(self.base_url, data=self.data_not_ok)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Некорректный email", response.text)

    def test_phone_correct(self):
        response = self.app.post(self.base_url, data=self.data_ok)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfully registered", response.text)

    def test_phone_incorrect(self):
        response = self.app.post(self.base_url, data=self.data_not_ok)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Номер телефона указан неверно", response.text)

    def test_name_correct(self):
        response = self.app.post(self.base_url, data=self.data_ok)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfully registered", response.text)

    def test_name_incorrect(self):
        response = self.app.post(self.base_url, data=self.data_not_ok)
        self.assertEqual(response.status_code, 400)
        self.assertIn("'name': ['Обязательно для заполнения']", response.text)

    def test_address_correct(self):
        response = self.app.post(self.base_url, data=self.data_ok)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfully registered", response.text)

    def test_address_incorrect(self):
        response = self.app.post(self.base_url, data=self.data_not_ok)
        self.assertEqual(response.status_code, 400)
        self.assertIn("'address': ['Обязательно для заполнения']", response.text)

    def test_index_correct(self):
        response = self.app.post(self.base_url, data=self.data_ok)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfully registered", response.text)

    def test_index_incorrect(self):
        response = self.app.post(self.base_url, data=self.data_not_ok)
        self.assertEqual(response.status_code, 400)
        self.assertIn("'index': ['Not a valid integer value.']", response.text)
