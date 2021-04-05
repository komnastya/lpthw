#Write a function which deletes from list all elements larger than max.

# Deletes from the given list all elements larger than max.
# Example: delete_large([1,2,3,4,5,6,7,8,1], 1) -> [1,1]
# Example: delete_large([1,2,3,4,5,6,7,8,1], 3) -> [1,2,3,1]
# Example: delete_large([1,2,3,4,5,6,7,8,9], 9) -> [1,2,3,4,5,6,7,8,9]
  # Write two implementations:
  # 1. An implementation which returns a new list.
  # 2. An implementation which modifies the given list and does not return anything.

def delete_large(list, max):
    output = []
    for x in list:
        if x <= max:
            output.append(x)
    return output

print('New list', delete_large([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

#This function change the list, and returns modified list, but does it slowly

def delete_large_slow(list, max):
    i = 0
    while i < len(list):
        if list[i] > max:
            del list[i]
        else:
            i = i + 1

nums = [10, 1, 11, 12, 2, 3, 4, 5, 13, 14, 15]
delete_large_slow(nums, 5)
print('Less than 10 -->', nums)


def delete_small(list, min):
    i = 0
    while i < len(list):
        if list[i] <= min:
            del list[i]
        else:
            i = i + 1


nums = [10, 1, 11, 12, 2, 3, 4, 5, 13, 14, 15]
delete_small(nums, 10)
print('More than 10 -->', nums)


def delete_large_fast(list, max):
    r = 0
    w = 0
    while r < len(list):
        value = list[r]
        r = r + 1
        if value < max:
            list[w] = value
            w = w + 1
    del list[w:]

nums = [10, 1, 11, 12, 2, 3, 4, 5, 13, 14, 15]
delete_large_fast(nums, 5)
print('Less than 5 (fast) -->', nums)


# Delete_large_fast function explanation -> -> ->

# 1

#      | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
#        r
# list | 1 | 7 | 4 | 6 | 8 | 3 | 2 | max = 5
#        w
#      | 0 |   |   |   |   |   |   |

# 2

#      | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
#            r
# list | 1 | 7 | 4 | 6 | 8 | 3 | 2 | max = 5
#            w
#      | 0 | 1 |   |   |   |   |   |

# 3

#      | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
#                r
# list | 1 | 4 | 4 | 6 | 8 | 3 | 2 | max = 5
#            w
#      | 0 | 1 |   |   |   |   |   |

# 4

#      | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
#                    r
# list | 1 | 4 | 4 | 6 | 8 | 3 | 2 | max = 5
#                w
#      | 0 | 1 |   |   |   |   |   |

# 5

#      | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
#                        r
# list | 1 | 4 | 4 | 6 | 8 | 3 | 2 | max = 5
#                w
#      | 0 | 1 |   |   |   |   |   |

# 6

#      | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
#                            r
# list | 1 | 4 | 3 | 6 | 8 | 3 | 2 | max = 5
#                w
#      | 0 | 1 | 2 |   |   |   |   |

# 7

#      | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
#                                r
# list | 1 | 4 | 3 | 2 | 8 | 3 | 2 | max = 5
#                    w
#      | 0 | 1 | 2 | 3 |   |   |   |
