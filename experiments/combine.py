from typing import List, Tuple


# Returns a new list containing all elements from both a and b such that
# the elements from a are in even positions, and
# the elements from b are in odd position.
# Both lists a and b are assumed to be of equal size.
# Example: combine([1], [4]) -> [1,4]
# Example: combine([1,2,3], [4,5,6]) -> [1,4,2,5,3,6]

# combine function is the equivalent to built-in zip function

def combine(a: List[int], b: List[int]) -> List[Tuple[int, int]]:
    if len(a) != len(b):
        raise ValueError
    output: List[Tuple[int, int]] = []
    for i in range(len(a)):
        output.append((a[i], b[i]))
    return output


def my_combine(a: List[int], b: List[int]) -> List[int]:
    if len(a) != len(b):
        raise ValueError
    output: List[int] = []
    for i, j in zip(a, b):  # or for i, j in combine(a,b)
        output.append(i)
        output.append(j)
    return output
