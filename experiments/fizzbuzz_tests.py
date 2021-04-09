import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
      self.assertFalse(fizz_buzz(0))
      self.assertEqual(fizz_buzz(1), [1])
      self.assertEqual(fizz_buzz(15), [1, 2, (3, 'fizz'), 4, (5, 'buzz'), (6, 'fizz'), 7, 8, (9, 'fizz'), (10, 'buzz'), 11, (12, 'fizz'), 13, 14, (15, 'fizz_buzz')])
      self.assertFalse(fizz_buzz(-1))
