# Sorts the given list of elements
# in the increasing order.
# TODO Implement me!
# loops
# ifs/conditions
# comparisons of list elements
# swapss
# list[1] < list[2]
# list[1] = list[2]


def is_sorted(list):
    if len(list) == 0:
        return False
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            return False
    return True
