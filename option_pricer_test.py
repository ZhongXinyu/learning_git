import unittest
from option_pricer import calculate_sum


class MyTestCase(unittest.TestCase):
    def test_calculate_sum(self):
        assert calculate_sum(1, 2) == 3

if __name__ == '__main__':
    unittest.main()