import unittest

from arpc import run


class TestCompile(unittest.TestCase):
    def test_str(self):
        result = run('api.arpc')
        print(result)
        self.assertIsInstance(result, str, "result is not str")

    def test_list(self):
        result = run(['api.arpc'])
        print(result)
        self.assertIsInstance(result, list, "result is not list")


if __name__ == '__main__':
    unittest.main()
