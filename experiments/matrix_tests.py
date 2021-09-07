import unittest

from matrix import is_square, matrix_sum


class TestMatrix(unittest.TestCase):

    def test_matrix(self):
        self.assertTrue(is_square([]))
        self.assertTrue(is_square([[1]]))
        self.assertTrue(is_square([[1, 2], [3, 4]]))
        # TODO self.assertFalse(is_square([[1],[2]]))

    def test_matrix_sum(self):
        self.assertEqual(matrix_sum([], []), [])
        self.assertEqual(matrix_sum([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]])
        # TODO self.assertFalse(matrix_sum([[1,2], [3,4]], [[1,2]]))


if __name__ == '__main__':
    unittest.main()
