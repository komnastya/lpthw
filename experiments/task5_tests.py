import unittest
from task5 import equal, flat, flat_2, split, delete_repeated, delete_repeated_2

class TestTask5(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(equal([],[]), True)
        self.assertEqual(equal([1],[1]), True)
        self.assertEqual(equal([1,2],[1,2]), True)
        self.assertEqual(equal([1,2,3],[1,2]), False)
        self.assertEqual(equal([1,2],[2,1]), False )

    def test_flat(self):
        self.assertEqual(flat([]),[])
        self.assertEqual(flat([[1], [2]]), [1,2])
        self.assertEqual(flat([[1,2,3],[4,5,6]]), [1,2,3,4,5,6])
        self.assertEqual(flat([[1],[2],[3],[4,5],[6]]), [1,2,3,4,5,6])

    def test_flat_2(self):
        self.assertEqual(flat([]),[])
        self.assertEqual(flat([[1], [2]]), [1,2])
        self.assertEqual(flat([[1,2,3],[4,5,6]]), [1,2,3,4,5,6])
        self.assertEqual(flat([[1],[2],[3],[4,5],[6]]), [1,2,3,4,5,6])

    def test_split(self):
        self.assertEqual(split([1,2,3], 1), [[1],[2],[3]])
        self.assertEqual(split([1,2,3], 2), [[1,2],[3]])
        self.assertEqual(split([1,2,3], 10), [[1,2,3]])
        self.assertEqual(split([1,2,3,4,5,6,7,8,9], 3), [[1,2,3],[4,5,6],[7,8,9]])

    def test_delete_repeated(self):
        self.assertEqual(delete_repeated([1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(delete_repeated([1,1,2,2,1,1]), [1,2,1])
        self.assertEqual(delete_repeated([1,1,1]), [1])

    def test_delete_repeated_2(self):
        self.assertEqual(delete_repeated_2([1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(delete_repeated_2([1,1,2,2,1,1]), [1,2,1])
        self.assertEqual(delete_repeated_2([1,1,1]), [1])


if __name__ == '__main__':
    unittest.main()
