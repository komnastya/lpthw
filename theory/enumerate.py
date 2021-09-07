# THEORY with examples


def numerate(list):
    for index in range(len(list)):
        value = list[index]
        print("Index is", index, "value is", value)


numerate([3, 5, 2, 3, 4, 6, 4])

print("\n")


# When you use enumerate(), the function gives you back two loop variables:

# ---The count of the current iteration -> index (line 16)
# ---The value of the item at the current iteration -> value (lime 16)


def in_built_enumerate(list):
    for index, value in enumerate(list):
        print(index, value)


in_built_enumerate([3, 5, 2, 7, 9, 4, 1, 6, 8])


# In this example, you pass start=1, which starts count with the value 1 on the first loop iteration

nums = [1, 5, 10, 15, 20, 25, 30, 35]

for index, value in enumerate(nums, start=1):
    print("Index is", index, "value is", value)


# Using conditional statements to process items can be a very powerful technique. Sometimes you might need to perform an action on only the very first iteration of a loop, as in this example:

users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    else:
        print(user)

# >>>
# Extra verbose output for: Test User
# Real User 1
# Real User 2


# You can also combine mathematical operations with conditions for the count or index. For instance, you might need to return items from an iterable, but only if they have an even index. You can do this by using enumerate():


def even_items(list):
    output = []
    for index, value in enumerate(list, start=1):
        if (
            not index % 2
        ):  # check whether the remainder of dividing index by 2 is zero. If it is, then you append the item to values.
            output.append(value)
    return output


def odd_items(list):  # нечет
    output = []
    for index, value in enumerate(list, start=1):
        if index % 2:
            output.append(value)
    return output


print(even_items([1, 2, 3, 4, 5, 6, 7]))


# create list of sequence
numbers = list(range(1, 20))

print(even_items(numbers))
print(odd_items(numbers))

alphabet = "abcdefghijklmnopqrstuvwxyz"

print(odd_items(alphabet))
print(even_items(alphabet))


# next()

values = ["a", "b"]  # create a list called values with two elements, "a" and "b"
enum_instance = enumerate(
    values
)  # pass values to enumerate() and assign the return value to enum_instance
print(
    enum_instance
)  # print enum_instance, you can see that it’s an instance of enumerate() with a particular memory address
print(
    next(enum_instance)
)  # built-in next() to get the next value from enum_instance. The first value that enum_instance returns is a tuple with the count 0 and the first element from values, which is "a".
print(
    next(enum_instance)
)  # calling next() again on enum_instance yields another tuple, this time with the count 1 and the second element from values, "b"

# Finally, calling next() one more time raises StopIteration since there are no more values to be returned from enum_instance.


# zip() allows to iterate through two or more sequences at the same time.

first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]
for one, two, three in zip(first, second, third):
    print(one, two, three)


# You can combine zip() and enumerate() by using nested argument unpacking:

for index, value in enumerate(first):
    print(index, value)

for index, (one, two, three) in enumerate(zip(first, second, third)):
    print(index, one, two, three)


# There are other ways to emulate the behavior of enumerate() combined with zip(). One method uses itertools.count(), which returns consecutive integers by default, starting at zero. You can change the previous example to use itertools.count():

import itertools

for count, one, two, three in zip(itertools.count(), first, second, third):
    print(count, one, two, three)
