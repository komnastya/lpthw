import unittest
from deleterepeated import delete_repeated, delete_repeated_2

class TestDeleteRepeated(unittest.TestCase):

    def test_delete_repeated(self):
        list = [1,2,3]
        delete_repeated(list)
        self.assertEqual(list, [1,2,3])

        list = [1,1,2,2,1,1]
        delete_repeated(list)
        self.assertEqual(list, [1,2,1])

        list = [1,1,1,1]
        delete_repeated(list)
        self.assertEqual(list, [1])

    def test_delete_repeated_2(self):
        self.assertEqual(delete_repeated_2([1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(delete_repeated_2([1,1,2,2,1,1]), [1,2,1])
        self.assertEqual(delete_repeated_2([1,1,1]), [1])


if __name__ == '__main__':
    unittest.main()
