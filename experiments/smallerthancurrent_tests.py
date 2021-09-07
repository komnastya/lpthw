import unittest

from smallerthancurrent import smallerNumbersThanCurrent, smallerNumbersThanCurrent_slow


class TestSmallerThanCurrent(unittest.TestCase):
    def test_smallerNumbersThanCurrent(self):
        self.assertEqual(smallerNumbersThanCurrent([]), [])
        self.assertEqual(smallerNumbersThanCurrent([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])
        self.assertEqual(smallerNumbersThanCurrent([1, 1, 1, 1]), [0, 0, 0, 0])
        self.assertEqual(smallerNumbersThanCurrent([9, 5, 3, 7, 11]), [3, 1, 0, 2, 4])

    def test_smallerNumbersThanCurrent_slow(self):
        self.assertEqual(smallerNumbersThanCurrent_slow([]), [])
        self.assertEqual(
            smallerNumbersThanCurrent_slow([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4]
        )
        self.assertEqual(smallerNumbersThanCurrent_slow([1, 1, 1, 1]), [0, 0, 0, 0])
        self.assertEqual(
            smallerNumbersThanCurrent_slow([9, 5, 3, 7, 11]), [3, 1, 0, 2, 4]
        )


if __name__ == "__main__":
    unittest.main()
