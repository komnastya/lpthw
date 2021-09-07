from typing import List

# Converts the given list of digits in a  given base.
# []            -> 0
# [0]           -> 0
# [1]           -> 1
# [1,0]         -> 10
# [1,2,3,4,5]   -> 12345


def digits_to_number(digits: List[int], base: int = 10) -> int:
    number = 0
    for digit in digits:
        number = number * base + digit
    return number


# Converts the given number to a list of digits in the given base.
# 0     -> [0]
# 1     -> [1]
# 10    -> [1,0]
# 12345 -> [1,2,3,4,5]


def number_to_digits(number: int, base: int = 10) -> List[int]:
    digits: List[int] = []
    if number == 0:
        digits.append(0)
    else:
        while number > 0:
            digits.insert(0, number % base)
            number = number // base
    return digits
