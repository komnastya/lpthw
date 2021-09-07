import unittest

from compress import compress, decompress, element_by_index


class TestDecompress(unittest.TestCase):
    def test_decompress(self):
        self.assertEqual(decompress([]), [])
        self.assertEqual(decompress([(1, 3)]), [1, 1, 1])
        self.assertEqual(decompress([(1, 1), (2, 1), (3, 1)]), [1, 2, 3])
        self.assertEqual(decompress([(1, 3), (2, 5)]), [1, 1, 1, 2, 2, 2, 2, 2])
        self.assertEqual(decompress([(999, 0)]), [])

    def test_compress(self):
        self.assertEqual(compress([]), [])
        self.assertEqual(compress([1, 1, 1]), [(1, 3)])
        self.assertEqual(compress([1, 2, 3]), [(1, 1), (2, 1), (3, 1)])
        self.assertEqual(
            compress([1, 1, 1, 2, 2, 2, 3, 3, 3]),  #
            [(1, 3), (2, 3), (3, 3)],
        )
        self.assertEqual(compress(""), [])
        self.assertEqual(compress("abc"), [("a", 1), ("b", 1), ("c", 1)])
        self.assertEqual(compress("aaa"), [("a", 3)])
        self.assertEqual(
            compress("aaabbbcccxxxxxxxxxx"), [("a", 3), ("b", 3), ("c", 3), ("x", 10)]
        )

    def test_element_by_index(self):
        self.assertEqual(element_by_index([(1, 3), (2, 3)], 1), 1)
        self.assertEqual(element_by_index([(1, 3), (2, 3)], 3), 2)
        self.assertEqual(element_by_index([(1, 3), (2, 3)], 6), None)


if __name__ == "__main__":
    unittest.main()
