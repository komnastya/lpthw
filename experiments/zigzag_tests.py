import unittest
from zigzag import zig_zag, zig_zag_2

class TestShift(unittest.TestCase):

    def test_zig_zag(self):
        self.assertEqual(zig_zag(-1), [])
        self.assertEqual(zig_zag(0), [0])
        self.assertEqual(zig_zag(1), [0,-1])
        self.assertEqual(zig_zag(5), [0,-1,2,-3,4,-5])

    def test_zig_zag_2(self):
        self.assertEqual(zig_zag_2(-1), [])
        self.assertEqual(zig_zag_2(0), [])
        self.assertEqual(zig_zag_2(1), [1,-1])
        self.assertEqual(zig_zag_2(5), [1,-1,2,-2,3,-3,4,-4,5,-5])


if __name__ == '__main__':
    unittest.main()
