import unittest

from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), [0, 1, 1])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci(15), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertFalse(fibonacci(-1))


if __name__ == '__main__':
    unittest.main()
