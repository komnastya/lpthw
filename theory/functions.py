# - Indexes vs elements.
# - Loops over elements.
# - Loops over indexes.

# Returns the maximal element from the given list.
# Example: [1,2,3,4,-1,-2] -> 4
def max_value(list):
    if len(list) == 0:
        return None
    maximal_value = list[0]
    for x in list:
        if x > maximal_value:
            maximal_value = x
    return maximal_value


def max_value_1(list):
    if len(list) == 0:
        return None
    maximal_value = list[0]
    for i in range(len(list)):
        x = list[i]
        if x > maximal_value:
            maximal_value = x
    return maximal_value


# Returns index of the maximal element from the given list.
# Example: [1,2,3,4,-1,-2] -> 3
def max_index(list):
    if len(list) == 0:
        return None
    maximal_value = list[0]
    maximal_index = 0
    for i in range(len(list)):
        x = list[i]
        if x > maximal_value:
            maximal_value = x
            maximal_index = i
    return maximal_index


# Returns the minimal element from the given list.
# Example: [1,2,3,4,-1,-2] -> -2
def min_value_1(list):
    if len(list) == 0:
        return None
    minimal = list[0]
    for x in list:
        if x < minimal:
            minimal = x
    return minimal


def min_value_2(list):
    if len(list) == 0:
        return None
    minimal = list[0]
    for i in range(len(list)):
        x = list[i]
        if x < minimal:
            minimal = x
    return minimal


# Returns index of the minimal element from the given list.
# Example: [1,2,3,4,-1,-2] -> 5
def min_index(list):
    if len(list) == 0:
        return None
    minimal_value = list[0]
    minimal_index = 0
    for i in range(len(list)):
        x = list[i]
        if x < minimal_value:
            minimal_value = x
            minimal_index = i
    return minimal_index


# Tests if the given list is sorted.
# Example: [0,1,2,3] -> True
# Example: [0,0,0,0] -> True
# Example: [0,1,2,0] -> False
def is_sorted(list):
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            return False
    return True


def print_list_1(list):
    for i in list:
        print(i)


def print_list_2(list):
    for i in range(len(list)):
        print(list[i])


def print_list_3(list):
    i = 0
    while i < len(list):
        print(list[i])
        i = i + 1


def print_list_4(list):
    i = 0
    while True:
        if i < len(list):
            print(list[i])
            i = i + 1
        else:
            break


def print_reveresed_1(list):
    i = 0  # increasing
    while i < len(list):
        print(list[len(list) - 1 - i])
        i = i + 1


def print_reveresed_2(list):
    i = len(list) - 1
    while i >= 0:
        print(list[i])
        i = i - 1


def print_except_first(list):
    i = 1
    while i < len(list):
        print(list[i])
        i = i + 1


def print_except_first_for_1(list):
    for i in range(1, len(list)):
        print(list[i])


def print_except_first_for_2(list):
    for i in range(len(list) - 1):
        print(list[i + 1])


def print_except_last(list):
    i = 0
    while i < len(list) - 1:
        print(list[i])
        i = i + 1


def print_except_last_for(list):
    for i in range(len(list) - 1):
        print(list[i])


def print_even_for(list):
    for i in range(0, len(list), 2):
        print(list[i])


def print_even_while(list):
    i = 0
    while i < len(list):
        print(list[i])
        i = i + 2


def print_odd_for(list):
    for i in range(1, len(list), 2):
        print(list[i])


def print_odd_while(list):
    i = 1
    while i < len(list):
        print(list[i])
        i = i + 2


print("Maximal value is", max_value_1([1, 2, 3, 4, -1, -2]))
print("Maximal index is", max_index([1, 2, 3, 4, -1, -2]))
print("Minimal value is", min_value_1([1, 2, 3, 4, -1, -2]))
print("Maximal index is", min_index([1, 2, 3, 4, -1, -2]))
print("Is the list sorted? It is ", is_sorted([1, 2, 3, 4]))
print("Is the list sorted? It is ", is_sorted([4, 3, 2, 1]))
print("Is the list sorted? It is ", is_sorted([7, 6, 5, 4, 1]))
print("Is the list sorted? It is ", is_sorted([7, 5, 3, 5, 7]))
print("Is the list sorted? It is ", is_sorted([1, 3, 5, 7, 5, 3, 1]))

# To practice with tuples and the enumerate function, write functions max_index, min_index using the enumerate function internally.


def max_index_2(list):
    if len(list) == 0:
        return False
    maximal = list[0]
    for index, value in enumerate(list):
        if value > maximal:
            maximal = value
            maximal_index = index
    return maximal_index


def min_index_2(list):
    if len(list) == 0:
        return False
    minimal = list[0]
    for index, value in enumerate(list):
        if value < minimal:
            minimal = value
            minimal_index = index
    return minimal_index


print(max_index_2([15, 3, 5, 1, 12, 4, 19, 7]))
#                                 ^ max element, index = 6
print(min_index_2([15, 3, 5, 1, 12, 4, 19, 7]))
#                          ^ min element, index = 3
print(min_index_2((15, 3, 5, 1, 12, 4, 19, 7)))  # This also works!
#                          ^ min element, index = 3
