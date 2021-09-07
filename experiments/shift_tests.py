# python -m unittest discover -p "*_test.py"

import unittest

from shift import shift_for, shift_while


class TestShift(unittest.TestCase):
    def test_shift_while(self):
        self.assertEqual(shift_while([]), [])
        self.assertEqual(shift_while([1]), [1])
        self.assertEqual(shift_while([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_shift_for(self):
        self.assertEqual(shift_for([]), [])
        self.assertEqual(shift_for([1]), [1])
        self.assertEqual(shift_for([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])


if __name__ == "__main__":
    unittest.main()
