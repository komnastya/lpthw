# ex33

i = 0  # define a variable with which we will fill the list
numbers = []  # define an empty list

while i < 5:  # cycle begins, which will run when i < 5
    print(f"\nNow i is {i}")  # the first nu,ber (0) is printed
    numbers.append(
        i
    )  # the number from line 7 is put into the list, this is its first element

    i = i + 1  # number + 1

    print(
        "\nNumbers now: ", numbers
    )  # contents of the array at the current moment is printed
    print(
        f"\nNext i is {i}"
    )  # the number which will be nested next to the array (from line 10)
    # the program goes back to line 7 until i <5


print("The numbers: ")

for num in numbers:  # elements of numbers list are printed
    print(num)
