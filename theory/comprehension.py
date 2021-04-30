squares = []
for i in range(10):
    squares.append(i * i)

print(squares)

# new_list = [expression for member in iterable] -> list comprehension

squares = [i * i for i in range(10)]
print("version 2", squares)

# new_list = [expression for member in iterable (if conditional)]


# You can place the conditional at the end of the statement for simple filtering, but what if you want to change a member value instead of filtering it out? In this case, it’s useful to place the conditional near the beginning of the expression:

# new_list = [expression (if conditional) for member in iterable]
