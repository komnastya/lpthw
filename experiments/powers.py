# Write a function which returns a list of all powers of two up to the max value (including):

# Returns a list of powers of two up to max (including):
# Example 1:  1 -> [1]
# Example 2: 10 -> [1, 2, 4, 8]
# Example 3: 32 -> [1, 2, 4, 8, 16, 32]

def powers_of_two (max):
  output = []
  value = 1
  while value <= max:
    output.append(value)
    value = value * 2
  return output


# Write a function which returns a list of all powers of three up to the max value (including) (in a different way):

# Returns a list of powers of three up to max (including):
# Example 1:  1 -> [1]
# Example 2: 10 -> [1, 3, 9, 27]
# Example 3: 32 -> [1, 3, 9, 27, 81, 243, 729]

def powers_of_three (max):
  output = []
  for power in range (max):
    value = 3 ** power
    if value <= max:
      output.append(value)
    else:
      break
  return output
