import unittest
from prime_number import PrimeNumber

class PrimeNumberTestCases(unittest.TestCase):

    def setUp(self):
        self.obj = PrimeNumber()

    def test_nonprime_number(self):
        result = self.obj.generate_prime_number(4)
        if result != 2:
            self.assertNotEqual(result % 2, 0)


if __name__ == '__main__':
    unittest.main()