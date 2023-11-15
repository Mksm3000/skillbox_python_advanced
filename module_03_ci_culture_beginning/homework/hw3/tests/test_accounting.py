import unittest


from module_03_ci_culture_beginning.homework.hw3.accounting import app, STORAGE


class TestAccounting(unittest.TestCase):

    @classmethod
    def setUp(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        STORAGE.update()

    def test_add(self):
        command = 'add'
        test_date = '20231102'
        test_money = '245'
        base_url = '/' + command + '/' + test_date + '/' + test_money
        response = self.app.get(base_url)
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode()
        self.assertTrue(test_money, 'успешно добавлены.' in response_text)

    def test_calculate_year(self):
        command = 'calculate'
        test_year = '2022'
        base_url = '/' + command + '/' + test_year
        response = self.app.get(base_url)
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode()
        self.assertTrue(f'Суммарные траты за {test_year} год' in response_text)

    def test_calculate_month(self):
        command = 'calculate'
        test_year = '2023'
        test_month = '11'
        base_url = '/' + command + '/' + test_year + '/' + test_month
        response = self.app.get(base_url)
        self.assertEqual(response.status_code, 200)
        response_text = response.data.decode()
        self.assertTrue(f'Суммарные траты за {test_year} год в {test_month} месяце' in response_text)


if __name__ == "__main__":
    unittest.main()
