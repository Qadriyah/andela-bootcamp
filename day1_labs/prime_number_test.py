import unittest
from prime_number import generate_prime_numbers


class PrimeNumberTestCases(unittest.TestCase):

    def test_negative_number(self):
        result = generate_prime_numbers(-5)
        self.assertEqual(
            'Only positive integers allowed',
            result,
            msg='The input number should be a positive integer')

    def test_for_empty_list(self):
        result = generate_prime_numbers(1)
        self.assertEqual(
            'Empty list of prime numbers',
            result,
            msg='The input number should be greater one')

    def test_if_list_is_generated(self):
        result = generate_prime_numbers(10)
        self.assertEqual(
            [2, 3, 5, 7],
            result,
            msg='To generate a list of prime numbers, the input should be greater than 1')

    def test_error_on_wrong_input(self):
        self.assertRaises(TypeError, generate_prime_numbers, '5')


if __name__ == '__main__':
    unittest.main()