import unittest
from datetime import datetime
from freezegun import freeze_time

from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import app, GREETINGS

COMPAIRS = (
    'понедельник',
    'вторник',
    'сред',
    'четверг',
    'пятниц',
    'суббот',
    'воскресен'
)


class TestHelloWorldWithDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_hello_with_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time("2023-12-12")
    def test_can_get_correct_day_of_week(self):
        username = 'username'
        weekday: int = datetime.today().weekday()
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertIn(COMPAIRS[weekday], response_text)

    def test_can_get_correct_input_in_username(self):
        username = 'Хорошей пятницы'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertNotIn(username, GREETINGS)
