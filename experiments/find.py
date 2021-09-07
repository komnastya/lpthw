from typing import Any, List


# Searches for the needle element
# in the haystak list,
# returns the first index of the found element
# or -1 if not found.
# The may be unsorted!
# Given list=[0,2,2,4], element=0, result=0
# Given list=[0,2,2,4], element=2, result=1
# Given list=[0,2,2,4], element=4, result=3
# Given list=[0,2,2,4], element=1, result=-1


def find(list: List[Any], element: Any) -> int:
  for i in range (len(list)):
    if list[i] == element:
      return i
  return -1
