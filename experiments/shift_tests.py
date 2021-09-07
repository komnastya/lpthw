# python -m unittest discover -p "*_test.py"
import unittest

from shift import shift_for, shift_inplace_smart, shift_inplace_stupid, shift_reverse, shift_slices, shift_while


class TestShift(unittest.TestCase):
    def test_shift_reverse(self):
        self.assertEqual(shift_reverse([]), [])
        self.assertEqual(shift_reverse([1]), [1])
        self.assertEqual(shift_reverse([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])

    def test_shift_while(self):
        self.assertEqual(shift_while([]), [])
        self.assertEqual(shift_while([1]), [1])
        self.assertEqual(shift_while([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_shift_for(self):
        self.assertEqual(shift_for([]), [])
        self.assertEqual(shift_for([1]), [1])
        self.assertEqual(shift_for([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_shift_slices(self):
        self.assertEqual(shift_slices([]), [])
        self.assertEqual(shift_slices([1]), [1])
        self.assertEqual(shift_slices([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_shift_inplace_smart(self):
        self.assertEqual(shift_inplace_smart([]), [])
        self.assertEqual(shift_inplace_smart([1]), [1])
        self.assertEqual(shift_inplace_smart([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])

    def test_shift_inplace_stupid(self):
        self.assertEqual(shift_inplace_stupid([]), [])
        self.assertEqual(shift_inplace_stupid([1, 2, 3, 4, 5]), [2, 3, 4, 5, 1])
        with self.assertRaises(ValueError):
            shift_inplace_stupid([0])
        with self.assertRaises(ValueError):
            shift_inplace_stupid([1])


if __name__ == "__main__":
    unittest.main()
