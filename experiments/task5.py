#LISTS

# - Write a function which tests whether lists are equal
#  i.e. each list_a[i] == list_b[i]:

# Tests whether the given matrix is square.
# Example: [], [] -> True
# Example: [1,2], [1,2] -> True
# Example: [[1,2], [2,1] -> False
# Example: [1,2], [1,2,3] -> False

def equal (a, b):
  if len(a) != len(b):
    return False
  for i in range (len(a)):
    if a[i] != b[i]:
      return False
  return True

print('eq', equal([], []), 'True')
print('eq', equal([1,2], [1,2]), 'True')
print('eq', equal([1,2], [1,3]), 'False')


#Write a function which takes a list of lists and returns a flat list as follows:

# Takes a list of lists and returns a flat list containg all the same
# elements from the nested lists:
# Example 1: [] -> []
# Example 2: [[1,2,3],[4,5,6]] -> [1,2,3,4,5,6]
# Example 3: [[1],[2],[3],[4,5],[6]] -> [1,2,3,4,5,6]
# Not a valid input: [[[1]]]

def flat(list_of_lists):
  output = []
  for l in list_of_lists:
    output.extend(l)
  return output

def flat_2(list_of_lists):
  output = []
  for l in list_of_lists:
    # This is very clear, readable and appealing,
    # but potentially is much slower than output.append(l)
    output = output + l
  return output

print (flat([[1, 2], [3, 4, 5, 6], [8, 9]]))
print (flat_2([[1, 2], [3, 4, 5, 6], [8, 9]]))


print ('Flat [1,2,[3,4],[5],6,[7,8,9]] is', flat([[1,2],[3],[4],[5],[6,7,8,9]]) )


#Write a function which splits a list into sublists of a fixed size:

# Example 1: split([1,2,3], 1) -> [[1],[2],[3]]
# Example 2: split([1,2,3], 2) -> [[1,2],[3]]
# Example 3: split([1,2,3], 10) -> [[1,2,3]]
# Example 4: split([1,2,3,4,5,6,7,8,9], 3) -> [[1,2,3],[4,5,6],[7,8,9]]
  # 1. create an inner list
  # 2. append elements to it while its len < max_size

def split(list, max_size):
  output = []
  for i in range (0, len(list), max_size):
    output.append(list[i:i+max_size])
  return output

print ('[[1,2,3],[4,5,6],[7,8,9]] is', split([1,2,3,4,5,6,7,8,9,10], 3))


#Write a function which deletes repeated elements from a list:

# Deletes repeated elements from the given list.
# Returns a new list.
# Example [1,2,3,4,5] -> [1,2,3,4,5]
# Example [1,1,1] -> [1]
# Example [1,1,2,2,1,1] -> [1,2,1]

def delete_repeated(list):
  i = 0
  while i < len(list) - 1:
    if list[i] == list[i + 1]:
      list[i:i+1] = []
    else:
      i = i + 1
  return list

def delete_repeated_2(list):
  output = []
  if len(list) == 0:
    return output
  output.append(list[0])
  i = 1
  while i < len(list):
    if list[i - 1] != list[i]:
      output.append(list[i])
    i = i + 1
  return output

print (delete_repeated([1,2,3,3,3,4,5,5,5]))
print ("--------------")
print (delete_repeated_2([]))
print (delete_repeated_2([1]))
print (delete_repeated_2([1,1,1]))
print (delete_repeated_2([1,2,3]))
print (delete_repeated_2([1,1,1,2,2,2,3,3,3]))
print (delete_repeated_2([1,2,3,3,3,4,5,5,5]))
