import unittest
from sort import is_sorted

class TestSort(unittest.TestCase):

    def test_is_sorted(self):
        self.assertFalse(is_sorted([]))
        self.assertTrue(is_sorted([1]))
        self.assertTrue(is_sorted([1,2]))
        self.assertFalse(is_sorted([3,2,1]))

if __name__ == '__main__':
    unittest.main()
