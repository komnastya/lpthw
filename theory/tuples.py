#Theory with examples

# Accessing tuple elements using slicing
my_tuple = ('n','a','s','t','a','s','s','i','a')

# elements 2nd to 4th
# Output: ('a', 's', 't')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('n', 'a')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'a')
print(my_tuple[7:])

# elements beginning to end
# Output: ('n','a','s','t','a','s','s','i','a')
print(my_tuple[:])


# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])

# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)

#We can use + operator to combine two tuples. This is called concatenation.

#We can also repeat the elements in a tuple for a given number of times using the * operator.

#Both + and * operations result in a new tuple.

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

#As discussed above, we cannot change the elements in a tuple. It means that we cannot delete or remove items from a tuple.

#Deleting a tuple entirely, however, is possible using the keyword del.

# Deleting tuples
my_tuple_2 = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple_2

# NameError: name 'my_tuple_2' is not defined
print(my_tuple)

#Methods that add items or remove items are not available with tuple. Only the following two methods are available.

#Some examples of Python tuple methods:

my_tuple_3 = ('a', 'p', 'p', 'l', 'e',)

# !!! COUNT tuple elements !!!
print(my_tuple_3.count('p'), '\'p\' is in \'apple\'')  # Output: 2

# !!! SHOW element index !!!
print('l is the', my_tuple_3.index('l') + 1, 'letter')  # Output: 3

#Other Tuple Operations
# -- 1 -- Tuple Membership Test
# We can test if an item exists in a tuple or not, using the keyword in.

# Membership test in tuple
fruit = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in fruit)
print('b' in fruit)

# Not in operation
print('g' not in fruit)

# -- 2 -- Iterating Through a Tuple
#We can use a for loop to iterate through each item in a tuple.

# Using a for loop to iterate through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)

#Output
#>>> Hello John
#>>> Hello Kate

#FUNCTIONS
tuple_1 = ('n', 'a', 's', 't', 'y', 'a')

#Gives the total length of the tuple.

print ("Tuple lenght is", len(tuple_1))

numbers = (1, 2, 3, 4, 5, 7, 9, 6, 8)
# Returns item from the tuple with max value.
print ('Maximal tuple value is', max(numbers))

# Returns item from the tuple with min value.
print ('Minimal tuple value is', min(numbers))


#a.insert(<index>, <obj>) inserts object <obj> into list a at the specified <index>. Following the method call, a[<index>] is <obj>, and the remaining list elements are pushed to the right:

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.insert(3, 3.14159)
print ('a with inserted 3 element is', a[3])
#>>> ['foo', 'bar', 'baz', 3.14159, 'qux', 'quux', 'corge']


# a.remove(<obj>) removes object <obj> from list a. If <obj> isn’t in a, an exception is raised:

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.remove('baz')
print ('a with removed \'baz\' is', a)
# >>> ['foo', 'bar', 'qux', 'quux', 'corge']

#a.remove('Bark!')
# >>>
# #Traceback (most recent call last):
#  File "<pyshell#13>", line 1, in <module>
#    a.remove('Bark!')
#ValueError: list.remove(x): x not in list

t = ()
print ('t type is', type(t))

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[5::-3])
['quux', 'baz', 'foo']
