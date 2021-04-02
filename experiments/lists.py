fruits = ['apple', 'pear', 'orange', 'banana', 'grapes', 'apricon']
#	reverse list
print (fruits[::-1])


#	delete list item
del fruits[3] #banana
print ('Fruits are ', fruits)


#	modify multiply list value
#list_name[m:n] = <iterable>

vegetables = ['potato', 'cucumber', 'tomato', 'carrot', 'onion']
print ('Vegetables are ', vegetables)

vegetables[0:2] = ['beet', 'pumpkin']

print ('Vegetables are ', vegetables)

vegetables[3:6] = ['Foo!']
print ('Vegetables are ', vegetables)


nums = [1, 2, 3, 4]
print ('Numbers are', nums)

nums[1:2] = [2.1, 2.2, 2.3]
print ('Numbers are', nums)

#Note that this is not the same as replacing the single element with a list:
nums = [1, 2, 3]
nums [1] = [2.1, 2.2, 2.3]
print ('Numbers are', nums)

#You can also insert elements into a list without removing anything. Simply specify a slice of the form [n:n] (a zero-length slice) at the desired index:

a = [1, 2, 7, 8]
a[2:2] = [3, 4, 5, 6]

print ('a is', a)

#You can delete multiple elements out of the middle of a list by assigning the appropriate slice to an empty list. You can also use the del statement with the same slice:

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[1:5] = []

print ('a is', a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
del a[1:5]
print ('a is', a)

#Additional items can be added to the start or end of a list using the + concatenation operator or the += augmented assignment operator:

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

a += ['grault', 'garply']

print ('New a is', a)

#>>> ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']

b = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

b = [10, 20] + b

print ('New b is', b)

#>>> [10, 20, 'foo', 'bar', 'baz', 'qux', 'quux', 'corge']

#Note that a list must be concatenated with another list, so if you want to add only one element, you need to specify it as a singleton list:

c = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# c += 20
#Traceback (most recent call last):
  #File "<pyshell#58>", line 1, in <module>
  # a += 20
#TypeError: 'int' object is not iterable

c += [20]
print ('New c is', c)

#>>> ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 20]

#Strings are iterable also. But watch what happens when you concatenate a string onto a list:

g = ['foo', 'bar', 'baz', 'qux', 'quux']
g += 'corge'

print ('New g is', g)

# >>> ['foo', 'bar', 'baz', 'qux', 'quux', 'c', 'o', 'r', 'g', 'e']

#This result is perhaps not quite what you expected. When a string is iterated through, the result is a list of its component characters. In the above example, what gets concatenated onto list a is a list of the characters in the string 'corge'.

#If you really want to add just the single string 'corge' to the end of the list, you need to specify it as a singleton list:

g = ['foo', 'bar', 'baz', 'qux', 'quux']
g += ['corge']
print ('New second g is', g)

# >>> ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']


#a.extend(<iterable>) extends a list with the objects from an iterable.

#Yes, this is probably what you think it is. .extend() also adds to the end of a list, but the argument is expected to be an iterable. The items in <iterable> are added individually:

a = ['a', 'b']
a.extend([1, 2, 3])
print ('Extended a is', a)

# >>> ['a', 'b', 1, 2, 3]
