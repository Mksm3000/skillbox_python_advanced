import unittest

from module_03_ci_culture_beginning.homework.hw4.person import Person


class TestPerson(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.test_person = Person('Alex', 1979, 'Tallinn')

    def test_get_age(self):
        expected_age = 44
        test_age = self.test_person.get_age()
        self.assertIsInstance(test_age, int)
        self.assertEqual(expected_age, test_age)

    def test_get_name(self):
        expected_name = 'Alex'
        test_name = self.test_person.get_name()
        self.assertIsInstance(test_name, str)
        self.assertEqual(expected_name, test_name)

    def test_set_name(self):
        expected_name = 'Michael'
        self.test_person.set_name(expected_name)
        test_name = self.test_person.get_name()
        self.assertEqual(expected_name, test_name)

    def test_set_address(self):
        expected_address = 'London'
        self.test_person.set_address(expected_address)
        test_address = self.test_person.get_address()
        self.assertEqual(expected_address, test_address)

    def test_get_address(self):
        expected_address = 'Tallinn'
        test_address = self.test_person.get_address()
        self.assertEqual(expected_address, test_address)

    def test_is_homeless(self):
        expected_answer = False
        result = self.test_person.is_homeless()
        self.assertIs(result, False)
        self.assertEqual(expected_answer, result)
