import unittest

from combine import combine, my_combine


class TestCombine(unittest.TestCase):

    def test_exception(self):
        with self.assertRaises(ValueError):
            my_combine([1], [1, 2])
        with self.assertRaises(ValueError):
            combine([1], [1, 2])

    def test_my_combine(self):
        self.assertEqual(my_combine([], []), [])
        self.assertEqual(my_combine([1], [1]), [1, 1])
        self.assertEqual(my_combine([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_combine(self):
        self.assertEqual(combine([], []), [])
        self.assertEqual(combine([1], [1]), [(1, 1)])
        self.assertEqual(combine([1, 3, 5], [2, 4, 6]), [(1, 2), (3, 4), (5, 6)])


if __name__ == "__main__":
    unittest.main()
