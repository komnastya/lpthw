# Theory

# Private method


class ClassName:
    def fun(self):
        print("Public method")

    def __fun(self):
        print("Private method")


a = ClassName()
a.fun()
a._ClassName__fun()  # call private method


# Catching and handling exceptions

try:
    x = int(input("Please enter a number: "))
    y = 100 / x
except ValueError:
    print("Error: there was an error")
except ZeroDivisionError:
    print("Error: 0 is an invalid number")
except Exception:
    print("Error: another error occurred")
finally:
    print("Cleanup can go here")

# Don’t declare new variables inside a try statement that might not be reached.

# x = 0 -> z will be undeclared
x = 10
try:
    y = 100 / x
    z = 23 * y
except ZeroDivisionError:
    pass
print(z)  # z will not be printed if an Exception is raised


# You might want to re-raise an exception to abort a script. For example, if we can’t determine what kind of error is causing the exception, we might want to re-raise it:

try:
    x = int(input("Please enter a number: "))
    y = 100 / x
except ValueError:
    print("Error: there was an error")
except ZeroDivisionError:
    print("Error: 0 is an invalid number")
except Exception:
    raise

print()

# It’s also possible to create a custom exception class that inherits from the base Exception class. A custom class might be needed if the developer wishes to integrate a more sophisticated logging system or further inspect an object.
# The __init__() and __str__() methods are required when defining an Exception class:


class CustomError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Error: %s" % self.value


try:
    raise CustomError("something went wrong")

except CustomError as e:
    print(e)

# Assertions evaluate an expression to true or false. If the expression is false, python will raise an AssertionError exception. Assertions can serve as a powerful developer tool when testing your code.

# The syntax for assertions is assert Expression[, Arguments]:
a = 3
assert a < 10, "a is more than 10"
# The code above will throw this error:
# Traceback (most recent call last):
#  File "file.py", line 2, in <module>
#    assert a < 10,  "something went wrong"
# AssertionError: something went wrong


class MyError(Exception):
    def __init__(self, text, num):
        self.txt = text
        self.n = num


a = input("Input positive integer: ")

try:
    a = int(a)
    if a < 0:
        raise MyError("You give negative!", a)
except MyError as mr:
    print(mr)
    print(mr.args)
    print(mr.args[0])
    print(mr.args[1])
else:
    print(a)
