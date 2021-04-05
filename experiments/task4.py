# Numbers vs. sequences

# Fibonacci sequence

# Write a function that returns a fibonacci list to max number as follows:
# 0,1,1,2,3,5,8,13,...,max

def fibonacci (max):
  a = 0
  b = 1
  print (a)
  print (b)
  while True:
    c = a + b
    if c > max:
      break
    print (c)
    a = b
    b = c

fibonacci (35)


# Write function fizz_buzz which works as follows:

# For every number in range 1..100:
# a) If the number is divisible by both 3 and 5, print “fizz-buzz”
# b) Otherwise If the number is divisible by 3, print “fizz”
# c) Otherwise If the number is divisible by 5, print “buzz”
# d) Otherwise print the number.
def fizz_buzz(max):
    for x in range(1, max + 1):
        if x % 15 == 0:
            print('fizz_buzz', x)
        elif x % 3 == 0:
            print('fizz', x)
        elif x % 5 == 0:
            print('buzz', x)
        else:
            print(x)


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
