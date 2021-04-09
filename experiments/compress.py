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


def element_by_index_2(list, index):
  for value, count in list:
    if count <= index:
      index = index - count
    else:
      return value
