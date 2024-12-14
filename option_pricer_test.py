import unittest
from option_pricer import calculate_sum, hello


class MyTestCase(unittest.TestCase):
    def test_calculate_sum(self):
        assert calculate_sum(1, 2) == 3

    def test_hello(self):
        assert hello() == "hello"


if __name__ == '__main__':
    unittest.main()