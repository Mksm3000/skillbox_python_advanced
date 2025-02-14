import io
import sys
import unittest
from module_05_processes_and_threads.homework.hw4.redirect import Redirect


class TestRedirect(unittest.TestCase):

    def setUp(self):
        self.test_file_stream = sys.stdout
        # self.test_file_stream = sys.stderr
        self.redirect = Redirect()

    def test_define_type(self):
        self.assertIsInstance(sys.stdout, io.IOBase)

    def test_is_empty(self):
        self.assertIsNone(self.redirect.stderr)


if __name__ == '__main__':

    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
