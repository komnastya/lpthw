# Converts the given list of digits in base 10 to a number.
# []            -> 0
# [0]           -> 0
# [1]           -> 1
# [1,0]         -> 10
# [1,2,3,4,5]   -> 12345
# Converts the given list of digits in base 10 to a number.
# []            -> 0
# [0]           -> 0
# [1]           -> 1
# [1,0]         -> 10
# [1,2,3,4,5]   -> 12345

def digits_to_number(digits, base=10):
    number = 0
    for digit in digits:
        number = number * base + digit  # good!
    return number


# Converts the given number to a list of digits in base 10.
# 0     -> [0]
# 1     -> [1]
# 10    -> [1,0]
# 12345 -> [1,2,3,4,5]

def number_to_digits(number, base=10):
    digits = []
    if number == 0:
        digits.append(0)
    else:
        while number > 0:
            digits.insert(0, number % base)
            number = number // base
    return digits
