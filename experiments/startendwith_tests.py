import unittest
from startendwith import starts_with, ends_with


class TestStartEndWith(unittest.TestCase):
    def test_starts_with(self):
        self.assertTrue(starts_with([1, 2, 3], []))
        self.assertTrue(starts_with([1, 2, 3], [1]))
        self.assertTrue(starts_with([1, 2, 3], [1, 2]))
        self.assertTrue(starts_with([1, 2, 3], [1, 2, 3]))
        self.assertFalse(starts_with([1, 2, 3], [2]))
        self.assertFalse(starts_with([1, 2, 3], [1, 2, 3, 4]))

    def tests_ends_with(self):
        self.assertTrue(ends_with([1, 2, 3], []))
        self.assertTrue(ends_with([1, 2, 3], [3]))
        self.assertTrue(ends_with([1, 2, 3], [2, 3]))
        self.assertTrue(ends_with([1, 2, 3], [1, 2, 3]))
        self.assertFalse(ends_with([1, 2, 3], [2]))
        self.assertFalse(ends_with([1, 2, 3], [1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()
