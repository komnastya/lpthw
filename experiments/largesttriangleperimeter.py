from typing import List


# Given an integer array nums, return the largest perimeter of a triangle
# with a non-zero area, formed from three of these lengths. If it is
# impossible to form any triangle of a non-zero area, return 0.

# Example: [] -> 0
# Example: [1, 2, 1] -> 0
# Example: [2, 1, 2] -> 5
# Example: [3, 2, 3, 4] -> 10
# Example: [3, 6, 2, 3] -> 8


def largestPerimeter(nums: List[int]) -> int:
    nums.sort(reverse=True)
    largest_perimeter: int = 0
    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            largest_perimeter = nums[i] + nums[i + 1] + nums[i + 2]
            return largest_perimeter
    return largest_perimeter
