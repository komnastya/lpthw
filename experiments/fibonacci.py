# Fibonacci sequence

# Write a function that returns a fibonacci list to max number as follows:
# 0,1,1,2,3,5,8,13,...,max

def fibonacci (max):
  if max <= 0:
    return False
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
