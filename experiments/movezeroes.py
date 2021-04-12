#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

#Example 1: [0,1,0,1,0] -> [1,1,0,0,0]
#Example 2: [1,1,1,0,0] -> [1,1,1,0,0]
#Example 3: [1,1,1,1,1] -> [1,1,1,1,1]
#Example 4: [] -> []

def moveZeroes(nums):
  r = 0
  w = 0
  while r < len(nums):
    value = nums[r]
    r = r + 1
    if value != 0:
      nums[w] = value
      w = w + 1
  while w < r:
    nums[w] = 0
    w = w + 1
