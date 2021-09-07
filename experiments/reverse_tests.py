import unittest

from reverse import reverse


class TestReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse([]), [])
        self.assertEqual(reverse([1]), [1])
        self.assertEqual(reverse([1, 2]), [2, 1])
        self.assertEqual(reverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
