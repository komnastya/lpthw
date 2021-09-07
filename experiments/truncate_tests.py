import unittest

from truncate import truncate


class TestTruncate(unittest.TestCase):
    def test_truncate(self):
        self.assertEqual(truncate([], 3), [])
        self.assertEqual(truncate([1, 2, 3, 4, 5, 6], 3), [1, 2, 3])
        self.assertEqual(truncate([1, 2, 3, 4, 5, 6], 0), [])
        self.assertEqual(truncate([1, 2, 3], 1_000_000), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
