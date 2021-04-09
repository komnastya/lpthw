# For every number in range 1..100:
# a) If the number is divisible by both 3 and 5, print “fizz-buzz”
# b) Otherwise If the number is divisible by 3, print “fizz”
# c) Otherwise If the number is divisible by 5, print “buzz”
# d) Otherwise print the number.
def fizz_buzz(max):
    if max <= 0:
        return False
    output = []
    for x in range(1, max + 1):
        if x % 15 == 0:
            output.append((x, 'fizz buzz'))
        elif x % 3 == 0:
            output.append((x,'fizz'))
        elif x % 5 == 0:
            output.append((x,'buzz'))
        else:
            output.append(x)
    return output


def fizz_buzz_2(max):
    a = 3
    b = 5
    c = 15
    for x in range(1, max + 1):
        if x == c:
            print('fizz_buzz', x)
            a += 3
            b += 5
            c += 15
        elif x == a:
            print('fizz', x)
            a += 3
        elif x == b:
            print('buzz', x)
            b += 5
        else:
            print(x)
