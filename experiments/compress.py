#compress()
#decompress()
#element_by_index()

# Takes a list of numbers and returns another list in which
# the repeated sequences of the same value are replaced
# with a pair (value, count).
# A pair (7, 9) means that number 7 repeats 9 times.
# A pair (3, 1) means that number 3 repeats 1 time.
# Example 1: [] -> []
# Example 2: [1, 1, 1] -> [(1, 3)]
# Example 3: [1, 2, 3] -> [(1, 1), (2, 1), (3, 1)]
# Example 4: [1, 1, 1, 2, 2, 2, 2, 2] -> [(1, 3), (2, 5)]
def compress(list):
    output = []
    if len(list) == 0:
        return output
    count = 1
    i = 0
    while i < len(list) - 1:
        if list[i] == list[i + 1]:
            count = count + 1
        else:
            output.append((list[i], count))
            count = 1
        i = i + 1
    output.append((list[i], count))
    return output


# Takes a compressed list of pairs (value, count) and decompresses it to a new list.
# Example 1: [] -> []
# Example 2: [(1, 3)] -> [1, 1, 1]
# Example 3: [(1, 1), (2, 1), (3, 1)] -> [1, 2, 3]
# Example 4: [(1, 3), (2, 5)] -> [1, 1, 1, 2, 2, 2, 2, 2]
# Example 5: [(999, 0)] -> []
def decompress(list):
    output = []
    for value, count in list:
        while count > 0:
            output.append(value)
            count = count - 1
    return output

# Takes a compressed list of pairs (value, count) and an index,
# then returns the element by the given index in a decompressed list.
# Example 1: [(1, 3), (2, 3)], 0 -> 1
# Example 2: [(1, 3), (2, 3)], 1 -> 1
# Example 3: [(1, 3), (2, 3)], 2 -> 1
# Example 4: [(1, 3), (2, 3)], 3 -> 2
# Example 5: [(1, 3), (2, 3)], 4 -> 2
# Example 6: [(1, 3), (2, 3)], 5 -> 2
# Example 7: [(1, 3), (2, 3)], 4 -> None

def element_by_index(list, index):
    sum = 0
    for value, count in list:
        sum = sum + count
        if index < sum:
            return value
    return None


# List of pairs (value[i], count[i]) splits the whole range
# into sub-intervals:
#
#
#  (v0,c0)  (v1,c1)  (v2,c2)  (v3,c3)  (v4,c4)
# +--------+--------+--------+---X----+--------+ len(list)
#          |        |        |   ↑    |        |
#          ^ sum0   |        |   ↑    |        |
#                   ^ sum1   |   ↑    |        |
#                            ^ sum2   |        |
#                                ↑    ^ sum3   |
#                                ↑             ^ sum4
#                                ↑
#                                ↑ index of the element to find
#
# We can scan the list of intervals from left to right, summing their lengths.
#
# If the index of the element to find is larger than or equal to the current
# running sum, it means we have not reached the desired interval yet.
#
# Otherwise if the index of the element to find is less than the current
# running sum, it means that the current interval contains the target element.
#
# In other words, the desired index is somewehere between two consecutive running sums.
#
# So the procedure is as follows:
# 1. For each pair (value, count):
# 2.  sum = sum + count
# 3.  if index < sum then return value


def element_by_index_buggy(list, index): #this function doesn't return None if index is out of range
    i = 0
    count = list[i][1] - 1
    while i < len(list) - 1:
        if index <= count:
            return list[i][0]
        else:
            count = count + list[i + 1][1]
        i = i + 1
