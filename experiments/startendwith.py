# Tests whether the given list starts|ends with the given PREFIX|SUFFIX

# Tests whether the given list starts with the given prefix.
# Example: starts_with([1,2,3], []) -> True
# Example: starts_with([1,2,3], [1]) -> True
# Example: starts_with([1,2,3], [1,2]) -> True
# Example: starts_with([1,2,3], [1,2,3]) -> True
# Example: starts_with([1,2,3], [2]) -> False
# Example: starts_with([1,2,3], [1,2,3,4]) -> False
def starts_with(list, prefix):
  if len(prefix) > len(list):
    return False
  for i in range (len(prefix)):
    if list[i] != prefix[i]:
      return False
  return True

# Write a function which tests if the given list ends with the given suffix:
# Tests whether the given list ends with the given suffix.
# Example: ends_with([1,2,3], []) -> True
# Example: ends_with([1,2,3], [3]) -> True
# Example: ends_with([1,2,3], [2,3]) -> True
# Example: ends_with([1,2,3], [1,2,3]) -> True
# Example: ends_with([1,2,3], [2]) -> False
# Example: ends_with([1,2,3], [0,1,2,3]) -> False

def ends_with(list, suffix):
  if len(suffix) > len(list):
    return False
  a = len(list) - len(suffix)
  for i in range (len(suffix)):
    if list[i + a] != suffix[i]:
      return False
  return True
