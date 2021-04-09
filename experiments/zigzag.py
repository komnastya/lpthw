# Write function zig_zag as follows

# Returns a list of numbers as follows:
# [0, -1, 2, -3, 4, -5, 6, -7, ..., max]
# i.e. all even values are positive,
# and all odd values are negative.

def zig_zag (max):
  output = []
  for x in range (max + 1):
    if x % 2:
      output.append(-x)
    else:
      output.append(x)
  return output


# Write function zig_zag as follows

# Returns a list of numbers as follows:
# [1, -1, 2, -2, 3, -3, ..., max]

def zig_zag_2 (max):
  output = []
  for x in range (1, max+1):
    output.append(x)
    output.append(-x)
  return output

print (zig_zag_2(2))
