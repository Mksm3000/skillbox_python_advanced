import unittest

from module_03_ci_culture_beginning.homework.hw2.decrypt import decryption

ASKS = ('абра-кадабра.', 'абраа..-кадабра', 'абраа..-.кадабра', 'абра--..кадабра', 'абрау...-кадабра', 'абра........', 'абр......a.',
        '1..2.3', '.', '1.......................')
ANSWERS = ('абра-кадабра', 'абра-кадабра', 'абра-кадабра', 'абра-кадабра', 'абра-кадабра', '', 'a', '23', '', '')


class TestDecrypt(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_answer_without_dots(self):
        for index in range(len(ASKS)):
            with self.subTest(i=index):
                result = decryption(ASKS[index])
                self.assertEqual(ANSWERS[index], result)


if __name__ == '__main__':
    unittest.main()
