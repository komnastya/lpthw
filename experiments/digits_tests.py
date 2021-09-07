import unittest

from digits import digits_to_number, number_to_digits


class TestDigits(unittest.TestCase):
    def test_DigitsToNumber(self):
        self.assertEqual(digits_to_number([]), 0)
        self.assertEqual(digits_to_number([0]), 0)
        self.assertEqual(digits_to_number([1]), 1)
        self.assertEqual(digits_to_number([1, 0]), 10)
        self.assertEqual(digits_to_number([1, 2, 3, 4, 5]), 12345)

    def test_NumberToDigits(self):
        self.assertEqual(number_to_digits(0), [0])
        self.assertEqual(number_to_digits(1), [1])
        self.assertEqual(number_to_digits(10), [1, 0])
        self.assertEqual(number_to_digits(12345), [1, 2, 3, 4, 5])
        self.assertEqual(number_to_digits(256, 2), [1, 0, 0, 0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
