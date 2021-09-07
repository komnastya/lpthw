import unittest
from deletelarger import (
    delete_large,
    delete_large_slow,
    delete_small,
    delete_large_fast,
)


class TestDeleteLarger(unittest.TestCase):
    def test_delete_large(self):
        self.assertEqual(delete_large([1, 2, 3, 4, 5, 6, 7, 8, 1], 1), [1, 1])
        self.assertEqual(delete_large([1, 2, 3, 4, 5, 6, 7, 8, 1], 3), [1, 2, 3, 1])
        self.assertEqual(
            delete_large([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

    def test_delete_large_slow(self):
        list = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]
        delete_large_slow(list, 10)
        self.assertEqual(list, [1, 2, 3, 4, 5])

        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        delete_large_slow(list, 5)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    def test_delete_small(self):
        list = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]
        delete_small(list, 10)
        self.assertEqual(list, [11, 12, 13, 14, 15])

        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        delete_small(list, 5)
        self.assertEqual(list, [6, 7, 8, 9, 10])

    def test_delete_large_fast(self):
        list = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]
        delete_large_fast(list, 10)
        self.assertEqual(list, [1, 2, 3, 4, 5])

        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        delete_large_fast(list, 5)
        self.assertEqual(list, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
