#ex33

i = 0
array = []

def myfun (a, n):
    b = 10
    if a < b:
        print (a)
    n.append(a)
    print (array)
    c = a + 1
    return c, n

a2, num2 = myfun (i, array)
a3, num3 = myfun (a2, num2)
a4, num4 = myfun (a3, num3)
