from typing import List


# Fibonacci sequence
def fibonacci(max: int) -> List[int]:
    if max <= 0:
        raise ValueError
    a = 0
    b = 1
    output = []
    output.append(a)
    output.append(b)
    while True:
        c = a + b
        if c > max:
            break
        output.append(c)
        a = b
        b = c
    return output
