from typing import List


# - Write a function which reverses a list:

# Reverses the given list.
# This function modifies the given list in-place,
# and does NOT return a new list.
# Example: [] -> []
# Example: [1] -> [1]
# Example: [1,2,3,4,5] -> [5,4,3,2,1]


def reverse(list: List[int]) -> List[int]:
    i = 0
    j = len(list) - 1
    while i < j:
        a = list[i]
        b = list[j]
        list[i] = b
        list[j] = a
        i = i + 1
        j = j - 1
    return list
