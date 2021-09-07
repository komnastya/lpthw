import unittest

from splitflat import equal, flat, split


class TestSplitFlat(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(equal([], []))
        self.assertTrue(equal([1], [1]))
        self.assertTrue(equal([1, 2], [1, 2]))
        self.assertFalse(equal([1, 2, 3], [1, 2]))
        self.assertFalse(equal([1, 2], [2, 1]))

    def test_flat(self):
        self.assertEqual(flat([]), [])
        self.assertEqual(flat([[1], [2]]), [1, 2])
        self.assertEqual(flat([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flat([[1], [2], [3], [4, 5], [6]]), [1, 2, 3, 4, 5, 6])

    def test_flat_2(self):
        self.assertEqual(flat([]), [])
        self.assertEqual(flat([[1], [2]]), [1, 2])
        self.assertEqual(flat([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flat([[1], [2], [3], [4, 5], [6]]), [1, 2, 3, 4, 5, 6])

    def test_split(self):
        self.assertEqual(split([1, 2, 3], 1), [[1], [2], [3]])
        self.assertEqual(split([1, 2, 3], 2), [[1, 2], [3]])
        self.assertEqual(split([1, 2, 3], 10), [[1, 2, 3]])
        self.assertEqual(
            split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        )


if __name__ == "__main__":
    unittest.main()
