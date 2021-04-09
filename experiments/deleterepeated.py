# Delete repeated elements from the given list.
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