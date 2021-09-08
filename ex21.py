# ex21


def add(a, b):
    print(f"Additing numbers {a} and {b} is ")
    return a + b


def substract(a, b):
    print(f"Substracting numbers {a} and {b} is")
    return a - b


def multiply(a, b):
    print(f"Multiplication numbers {a} and {b} is")
    return a * b


def divide(a, b):
    print(f"Dividing numbers {a} and {b} is")
    return a / b


print("Let's count!")

age = add(10, 14)
height = substract(200, 30)
weight = multiply(29, 2)
iq = divide(164, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here's a  puzzle")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

myexample = multiply(height, add(iq, multiply(age, 2)))

print("That becomes: ", what, "Can you do it by hand?")

print("My own exmple count like (age*2 + iq) * height = ", myexample)
