import unittest
from module_05_processes_and_threads.homework.hw3.block_errors import BlockErrors


class TestErrors(unittest.TestCase):

    def test_subclass(self):
        err_types = {ZeroDivisionError, TypeError}
        try:
            with BlockErrors(err_types):
                a = 1 / 0
        except Exception:
            self.assertTrue(issubclass(*err_types, Exception))

    def test_exception(self):
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors({TypeError}):
                result = 1 / 0


if __name__ == '__main__':
    unittest.main()
