import unittest

from largesttriangleperimeter import largestPerimeter


class TestLargetsTrianglePerimeter(unittest.TestCase):
    def test_find(self):
        self.assertEqual(largestPerimeter([]), 0)
        self.assertEqual(largestPerimeter([1, 2, 1]), 0)
        self.assertEqual(largestPerimeter([2, 1, 2]), 5)
        self.assertEqual(largestPerimeter([3, 2, 3, 4]), 10)
        self.assertEqual(largestPerimeter([3, 6, 2, 3]), 8)


if __name__ == "__main__":
    unittest.main()
