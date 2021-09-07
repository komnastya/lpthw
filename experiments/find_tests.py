import unittest

from find import find


class TestFind(unittest.TestCase):
    def test_find(self):
        self.assertEqual(find([], 1), -1)
        self.assertEqual(find([1, 1, 1, 1, 1], 1), 0)
        self.assertEqual(find([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(find([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(find([1, 2, 3, 4, 5], 0), -1)


if __name__ == "__main__":
    unittest.main()
