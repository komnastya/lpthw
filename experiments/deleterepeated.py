# Delete repeated elements from the given list.
# Returns a new list.
# Example [1,2,3,4,5] -> [1,2,3,4,5]
# Example [1,1,1] -> [1]
# Example [1,1,2,2,1,1] -> [1,2,1]
from typing import List


def delete_repeated(list: List[int]) -> None:
    i = 0
    while i < len(list) - 1:
        if list[i] == list[i + 1]:
            list[i : i + 1] = []
        else:
            i = i + 1


def delete_repeated_2(list: List[int]) -> List[int]:
    output: List[int] = []
    if len(list) == 0:
        return output
    output.append(list[0])
    i = 1
    while i < len(list):
        if list[i - 1] != list[i]:
            output.append(list[i])
        i = i + 1
    return output


def removeDuplicates(nums: List[int]) -> None:
    w = 0
    r = 0
    while r < len(nums):
        nums[w] = nums[r]
        w = w + 1
        r = r + 1
        while r < len(nums) and nums[r - 1] == nums[r]:
            r = r + 1
    del nums[w:]
