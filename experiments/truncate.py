# - Ensures that the given list is not longer than max_length:

# Example: truncate([], 3) -> []
# Example: truncate([1,2,3,4,5,6], 3) -> [1,2,3]
# Example: truncate([1,2,3,4,5,6], 0) -> []
# Example: truncate([1,2,3,4,5,6], 1000) ->


# TODO Implement me!
# Write two implementations:
# 1. An implementation which returns a new list.
# 2. An implementation which modifies the given list and does not return anything.

# first variant


def truncate(list, max_length):
    output = []
    if len(list) == 0:
        return output
    # elif len(list) < max_length:
    # return list # FIXME: неправильно, надо вернуть новый список, а не list
    # i = 0
    # while len(output) < max_length:
    #   output.append(list[i])
    #  i = i + 1
    for i in range(len(list)):
        if i < max_length:
            output.append(list[i])
    return output


# second variant


def truncate_2(list, max_length):
    del list[max_length:]


def truncate_3(list, max_length):
    if len(list) == 0:
        return list
    while len(list) > max_length:
        list.pop()  # OR del list[-1]
