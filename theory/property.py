# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter method
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

#human.temperature = -300

#The @property Decorator
#In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:

#property(fget=None, fset=None, fdel=None, doc=None)
#where,

#fget is function to get value of the attribute
#fset is function to set value of the attribute
#fdel is function to delete the attribute
#doc is a string (like a comment)
#As seen from the implementation, these function arguments are optional. So, a property object can simply be created as follows.

#>>> property()
#<property object at 0x0000000003239B38>
#A property object has three methods, getter(), setter(), and deleter() to specify fget, fset and fdel at a later point. This means, the line:

#temperature = property(get_temperature,set_temperature)
#can be broken down as:

# make empty property
temperature = property()
# assign fget
#temperature = temperature.getter(get_temperature)
# assign fset
#temperature = temperature.setter(set_temperature)
#These two pieces of codes are equivalent.

# Using @property decorator
class Celsius_2:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius_2(37)

print(human.temperature)

print(human.to_fahrenheit())
