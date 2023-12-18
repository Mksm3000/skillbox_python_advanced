import unittest
import subprocess
import shlex
from module_05_processes_and_threads.homework.hw2.remote_execution import app


class TestCode(unittest.TestCase):

    @classmethod
    def setUp(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        cls.base_url = '/run_code'
        cls.app = app.test_client()

        cls.data_ok = {'code': 'python -c "print(\'Test is well done\')"',
                       'timeout': 10
                       }

        cls.data_not_ok = {'code': 'python -c "wrong(\'Test is broken\')"',
                           'timeout': 32
                           }

    def test_run_python_code_in_sub_ok(self):
        code = self.data_ok['code']
        command = 'prlimit --nproc=1:1 ' + code
        clear = shlex.split(command)

        test_proc = subprocess.Popen(clear)
        test_proc.wait()
        self.assertEqual(test_proc.returncode, 0)

    def test_run_python_code_in_sub_not_ok(self):
        code = self.data_not_ok['code']
        command = 'prlimit --nproc=1:1 ' + code
        clear = shlex.split(command)

        test_proc = subprocess.Popen(clear)
        test_proc.wait()
        self.assertNotEqual(test_proc.returncode, 0)

    def test_run_code_ok(self):
        response = self.app.post(self.base_url, data=self.data_ok)
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"well done", response.text)

    def test_run_code_not_ok(self):
        response = self.app.post(self.base_url, data=self.data_not_ok)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
