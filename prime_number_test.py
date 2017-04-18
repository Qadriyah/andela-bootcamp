import unittest
from prime_number import PrimeNumber

class PrimeNumberTestCases(unittest.TestCase):

    def setUp(self):
        self.obj = PrimeNumber()

    def test_nonprime_number(self):
        result = self.obj.generate_prime_number(6)
        if result != 2:
            self.assertNotEqual(result % 2, 0)

    def test_noninteger_number(self):
        result = self.obj.generate_prime_number("5")
        self.assertIsInstance(result, int)

    def test_prime_number(self):
        result = self.obj.generate_prime_number(5)
        self.assertNotEqual(result % 2, 0)

    def test_negative_number(self):
        result = self.obj.generate_prime_number(5)
        self.assertLess(0, result)

    def test_error_on_wrong_input(self):
        self.assertRaises(TypeError, self.obj.generate_prime_number, '5')


if __name__ == '__main__':
    unittest.main()