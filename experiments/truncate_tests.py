import unittest

from truncate import truncate, truncate_2, truncate_3


class TestTruncate(unittest.TestCase):
    def test_truncate(self):
        self.assertEqual(truncate([], 3), [])
        self.assertEqual(truncate([1, 2, 3, 4, 5, 6], 3), [1, 2, 3])
        self.assertEqual(truncate([1, 2, 3, 4, 5, 6], 0), [])
        self.assertEqual(truncate([1, 2, 3], 1_000_000), [1, 2, 3])

    def test_truncate_2(self):
        nums = [1, 2, 3, 4, 5, 6]
        truncate_2(nums, 3)
        self.assertEqual(nums, [1, 2, 3])

        nums = [1, 2, 3, 4, 5, 6]
        truncate_2(nums, 0)
        self.assertEqual(nums, [])

        nums = [1, 2, 3, 4, 5, 6]
        truncate_2(nums, 1000)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

        nums = []
        truncate_2(nums, 1000)
        self.assertEqual(nums, [])

    def test_truncate_3(self):
        nums = [1, 2, 3, 4, 5, 6]
        truncate_3(nums, 3)
        self.assertEqual(nums, [1, 2, 3])

        nums = [1, 2, 3, 4, 5, 6]
        truncate_3(nums, 0)
        self.assertEqual(nums, [])

        nums = [1, 2, 3, 4, 5, 6]
        truncate_3(nums, 1000)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

        nums = []
        truncate_3(nums, 1000)
        self.assertEqual(nums, [])

if __name__ == "__main__":
    unittest.main()
