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
