# MATRIX

# - Write a function which tests whether a matrix (a list of lists) is square,
#  i.e. the number of columns in each row is the same as the number of rows:

# Tests whether the given matrix is square.
# Example: [] -> True
# Example: [[1]] -> True
# Example: [[1,2],[3,4]] -> True
# Example: [[1],[2]] -> False

def is_square (matrix):
  for row in matrix:
    if len(row) != len (matrix):
      return False
  return True

print ('\n ------------------> Is it square?')

print ('True -->', is_square([]))
print ('True -->', is_square([[1,2],[3,4]]))
print ('False -->', is_square([[1],[4]]))
print ('True -->', is_square([[1,2,3],[3,4,5], [5,6,7]]))
print ('False -->', is_square([[1,2,3,4],[3,4,5],[5,6,7,8], [1,1,1,1]]))
print ('True -->', is_square([[1,2,3,4],[3,4,5,6], [5,6,7,8], [1,1,1,1]]))


#Matrix addition

def matrix_sum(a, b):
  if len(a) != len(b):
    return False
  rows = []
  for i in range(len(a)):
    columns = []
    for j in range(len(a[i])):
      x = a[i][j] + b[i][j]
      columns.append(x)
    rows.append(columns)
  return rows

a = [
  [1, 2],
  [3, 4],
]
b = [
  [5, 6],
  [7, 8],
]

print(matrix_sum(a, b))
