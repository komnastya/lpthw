# Exceptions vs. Syntax Errors

# Syntax errors occur when the parser detects an incorrect statement, like  print (a)). There is one bracket too many.

# Exception error occurs whenever syntactically correct Python code results in an error. The last line of the message indicated what type of exception error you ran into.

# >>> print( 0 / 0)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# ZeroDivisionError: integer division or modulo by zero

# Instead of showing the message exception error, Python details what type of exception error was encountered. In this case, it was a ZeroDivisionError. Python comes with various built-in exceptions as well as the possibility to create self-defined exceptions.

x = 1
# x = 10
if x > 5:
    raise Exception("x should not exceed 5. The value of x was: {}".format(x))


# The try and except Block: Handling Exceptions

# The try and except block in Python is used to catch and handle exceptions. Python executes code following the try statement as a “normal” part of the program. The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.

# As you saw earlier, when syntactically correct code runs into an error, Python will throw an exception error. This exception error will crash the program if it is unhandled. The except clause determines how your program responds to exceptions.

# The following function can help you understand the try and except block:

import sys


def linux_interaction():
    assert "linux" in sys.platform, "Function can only run on Linux systems."
    print("Doing something.")


# The linux_interaction() can only run on a Linux system. The assert in this function will throw an AssertionError exception if you call it on an operating system other then Linux.

# You can give the function a try using the following code:

try:
    linux_interaction()
except:
    pass

# You got nothing. The good thing here is that the program did not crash. But it would be nice to see if some type of exception occurred whenever you ran your code. To this end, you can change the pass into something that would generate an informative message, like so:

try:
    linux_interaction()
except:
    print("Linux function was not executed")


# What you did not get to see was the type of error that was thrown as a result of the function call. In order to see exactly what went wrong, you would need to catch the error that the function threw.


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("The linux_interaction() function was not executed")


# In the previous example, you called a function that you wrote yourself. When you executed the function, you caught the AssertionError exception and printed it to screen.

# Here’s another example where you open a file and use a built-in exception:

try:
    with open("file.log") as file:
        read_data = file.read()
except:
    print("Could not open file.log")


# To catch this type of exception and print it to screen, you could use the following code:

try:
    with open("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)


# Imagine that you always had to implement some sort of action to clean up after executing your code. Python enables you to do so using the finally clause.
