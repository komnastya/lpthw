import unittest
from movezeroes import moveZeroes


class TestMoveZeroes(unittest.TestCase):
    def test_moveZeroes(self):
        nums = [0, 1, 0, 1, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 1, 0, 0, 0])

        nums = [1, 1, 1, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 1, 1, 0, 0])

        nums = [1, 1, 1, 1, 1]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 1, 1, 1, 1])

        nums = [0, 0, 0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
