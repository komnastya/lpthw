import unittest
from pascaltriangle import pascal_triangle, pascal_triangle_by_index

class TestPascalTriangle(unittest.TestCase):

    def test_PascalTriangle(self):
      self.assertEqual(pascal_triangle(-1), [])
      self.assertEqual(pascal_triangle(1), [[1]])
      self.assertEqual(pascal_triangle(2), [[1], [1,1]])
      self.assertEqual(pascal_triangle(3), [[1], [1,1], [1,2,1]])
      self.assertEqual(pascal_triangle(4), [[1], [1,1], [1,2,1], [1,3,3,1]])

    def test_PascalTriangleByIndex(self):
      self.assertEqual(pascal_triangle_by_index(0), [1])
      self.assertEqual(pascal_triangle_by_index(1), [1,1])
      self.assertEqual(pascal_triangle_by_index(2), [1,2,1])
      self.assertEqual(pascal_triangle_by_index(3), [1,3,3,1])

if __name__ == '__main__':
    unittest.main()
