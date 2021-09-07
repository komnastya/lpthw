# Field, Attribute, Property <- a variable inside of class

# What is class?
# It is a template which describes may objects if its type
# What is object? It is described by a class

# We declare an empty class.
class Empty:
    pass


# We declare a new data type.
class Person:
    # Constructor is a function which "creates" object of class Person.
    def __init__(self, name1, age1, health1):
        self.name = name1
        self.age = age1
        self.health = health1

    def print_data(self):
        print(self.name, " is", self.age, " old year person")

    def print_age(self):
        print(self.name, " has ", self.age, "years old")

    def rename(self, new_name):
        self.name = new_name


# if we do not write 'self.' before any variable inside a class, it is not clear what variable it is, for example, is it 'age' inside or outside class

alice = Person(
    "Alice", 13, 100
)  # calls class constructor and create a new object of type Person
bob = Person("Bob", 15, 50)
persons = [alice, bob]  # creates list with two objects


alice.print_data()  # prints line 20 with Alice's data
alice.print_age()

alice.rename("Eve")
alice.print_data()  # prints line 20 with Alice's renaamed data

eve = Person("Eve", 15, 90)
eve.print_data()  # prints line 20 with Eve's data
