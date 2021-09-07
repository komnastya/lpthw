from typing import List


# - Ensures that the given list is not longer than max_length:

# Example: truncate([], 3) -> []
# Example: truncate([1,2,3,4,5,6], 3) -> [1,2,3]
# Example: truncate([1,2,3,4,5,6], 0) -> []
# Example: truncate([1,2,3,4,5,6], 1000) ->


# Write two implementations:
# 1. An implementation which returns a new list.
# 2. An implementation which modifies the given list and does not return anything.

# first variant


def truncate(list: List[int], max_length: int) -> List[int]:
    output: List[int] = []
    if len(list) == 0:
        return output
    # elif len(list) < max_length:
    # return list
    # i = 0
    # while len(output) < max_length:
    #   output.append(list[i])
    #  i = i + 1
    for i in range(len(list)):
        if i < max_length:
            output.append(list[i])
    return output


# second variant


def truncate_2(list: List[int], max_length: int) -> None:
    del list[max_length:]


def truncate_3(list: List[int], max_length: int) -> None:
    while len(list) > max_length:
        list.pop()  # OR del list[-1]
