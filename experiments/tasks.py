# TASK 2

# Write a function which returns a list of all powers of two up to the max value (including):

# Returns a list of powers of two up to max (including):
# Example 1:  1 -> [1]
# Example 2: 10 -> [1, 2, 4, 8]
# Example 3: 32 -> [1, 2, 4, 8, 16, 32]
def powers_of_two_1(max):
  output = []
  for power in range(0):
    value = 2 ** power
    if value <= max:
      output.append(value)
    else:
      break
  return output

def powers_of_two_2(max):
  output = []
  value = 1
  while value <= max:
    output.append(value)
    value = value * 2
  return output

print('Powers of two which are less than or equal to 8: ', powers_of_two_2(8))
print('Powers of two which are less than or equal to 17: ', powers_of_two_2(17))
print('Powers of two which are less than or equal to 65: ', powers_of_two_2(65))
print('Powers of two which are less than or equal to 129: ', powers_of_two_2(129))
print('Powers of two which are less than or equal to 1024: ', powers_of_two_2(1024))


# Write function zig_zag as follows

# Returns a list of numbers as follows:
# [0, -1, 2, -3, 4, -5, 6, -7, ..., max]
# i.e. all even values are positive,
# and all odd values are negative.

def zig_zag(max):
  output = []
  for value in range(0, max + 1):
    if value % 2:
      output.append(-value)
    else:
      output.append(value)
  return output

print(zig_zag(10))


# Write a function which combines two lists as follows:

# Returns a new list containing all elements from both a and b such that
# the elements from a are in even positions, and
# the elements from b are in odd position.
# Both lists a and b are assumed to be of equal size.
# Example: combine([1], [4]) -> [1,4]
# Example: combine([1,2,3], [4,5,6]) -> [1,4,2,5,3,6]

def combine(a, b):#it likes in-build zip()
  output = []
  for i in range (len(a)):
    output.append((a[i], b[i]))
  return output


def my_combine(a, b):
  if len(a) != len(b):
    return False
  output = []
  for i, j in combine(a,b): #or for i, j in zip(a,b)
    output.append(i)
    output.append(j)
  return output

x = ['h', 'l', 'o', 'o', 'l']
y = ['e', 'l', 'w', 'r', 'd']

print (combine(x,y))

fst = ["n", "s", "y"]
snd = ["a", "t", "a"]

print (my_combine(fst, snd))


# - Write a function which reverses a list:

# Reverses the given list.
# This function modifies the given list in-place,
# and does NOT return a new list.
# Example: [] -> []
# Example: [1] -> [1]
# Example: [1,2,3,4,5] -> [5,4,3,2,1]
def reverse(list):
  i = 0
  j = len(list) - 1
  while i < j:
    a = list[i]
    b = list[j]
    list[i] = b
    list[j] = a
    i = i + 1
    j = j - 1
  return list

my_list = [1,2,3,4,5]
reverse (my_list)
print (my_list)
