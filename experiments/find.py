# Searches for the needle element
# in the haystak list,
# returns the first index of the found element
# or -1 if not found.
# The may be unsorted!
# Given list=[0,2,2,4], element=0, result=0
# Given list=[0,2,2,4], element=2, result=1
# Given list=[0,2,2,4], element=4, result=3
# Given list=[0,2,2,4], element=1, result=-1

def find(list, element):
  index = -1
  for i in range (len(list)):
    if list[i] == element:
      index = i
  return index

print ('0 =', find ([1,2,3,4,5,6,7], 1))
print ('2 =', find ([1,2,3,4,5,6,7], 3))
print ('4 =', find ([1,2,3,4,5,6,7], 5))
print ('-1 =', find ([1,2,3,4,5,6,7], 14))
print ('-1 =', find ([1,2,3,4,5,6,7], 0))
print ('-1 =', find ([1,2,3,4,5,6,7], 9))
