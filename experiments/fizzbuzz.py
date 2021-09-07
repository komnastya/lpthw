from typing import List, Literal, Tuple, Union

# For every number in range 1..100:
# a) If the number is divisible by both 3 and 5, print “fizz-buzz”
# b) Otherwise If the number is divisible by 3, print “fizz”
# c) Otherwise If the number is divisible by 5, print “buzz”
# d) Otherwise print the number.


FizzBuzzString = Union[
    Literal["fizz"],
    Literal["buzz"],
    Literal["fizz_buzz"],
]
FizzBuzzList = List[Union[int, Tuple[int, FizzBuzzString]]]


def fizz_buzz(max: int) -> FizzBuzzList:
    if max <= 0:
        return []
    output: FizzBuzzList = []
    for x in range(1, max + 1):
        if x % 15 == 0:
            output.append((x, "fizz_buzz"))
        elif x % 3 == 0:
            output.append((x, "fizz"))
        elif x % 5 == 0:
            output.append((x, "buzz"))
        else:
            output.append(x)
    return output


def fizz_buzz_2(max: int) -> FizzBuzzList:
    output: FizzBuzzList = []
    a = 3
    b = 5
    c = 15
    for x in range(1, max + 1):
        if x == c:
            output.append((x, "fizz_buzz"))
            a += 3
            b += 5
            c += 15
        elif x == a:
            output.append((x, "fizz"))
            a += 3
        elif x == b:
            output.append((x, "buzz"))
            b += 5
        else:
            output.append(x)
    return output
