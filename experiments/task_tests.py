import unittest
from task import my_combine, reverse

class TestTask(unittest.TestCase):

    def test_my_combine(self):
        self.assertEqual(my_combine([],[]), [])
        self.assertEqual(my_combine([1], [1]), [1,1])
        self.assertEqual(my_combine([1], [1,2]), False)
        self.assertEqual(my_combine([1,2], [1]), False)
        self.assertEqual(my_combine([1,3,5], [2,4,6]), [1,2,3,4,5,6])

    def test_reverse(self):
        self.assertEqual(reverse([]), [])
        self.assertEqual(reverse([1]), [1])
        self.assertEqual(reverse([1,2]), [2,1])
        self.assertEqual(reverse([1,2,3,4,5]), [5,4,3,2,1])


if __name__ == '__main__':
    unittest.main()
