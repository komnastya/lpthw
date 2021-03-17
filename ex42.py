#Ex. 42

#Animal is-a object look at the extra credit
class Animal (object):
    pass

#class Dog is-a object of class Animal
class Dog (Animal):
    def __init__(self, name):
        #class Dog has a __init___ that takes self and name parameters
        self.name = name
        print ("Dog's name is ", self.name)

#class Cat is-a object of class Animal
class Cat (Animal):
    def __init__(self, name):
        #class Cat has a __init___ that takes self and name parameters
        self.name = name
        print ("Cat's name is ", self.name)


#class Person is-a object
class Person(object):
    def __init__(self, name):
        #class Person has a __init___ that takes self and name parameters
        self.name = name
        #Person has-a pet of some kind
        self.pet = None
        print ("Person's name is ", self.name)
        print ("He/she has a pet - ", self.pet)


#class Employee is-a object of class Person
class Employee(Person):
    def __init__(self, name, salary):
        #class Employee has a __init___ that takes self, name, and salary parameters
        super(Employee, self).__init__(name)
        #
        self.salary = salary
        print ("Employee's name is ", self.name)
        print ("He/she has a salary - ", self.salary)



#class Fish is-a object
class Fish (object):
    pass

#class Salmon is-a Fish
class Salmon (Fish):
    pass

#Halibut is-a fish
class Halibut (Fish):
    pass

#Rover is-a dog
rover = Dog("Rover")

#satan is-a cat
satan = Cat("Satan")

#Mary is-a Person
mary = Person ("Mary")

#Mary has-a Satan
mary.pet = satan

#Frank is-a employee
frank = Employee("Frank", 120000)

#frank has-a pet Rover
frank.pet = rover

print ("Frank has a pet named ", rover.name)

#flipper is-a Fish
flipper = Fish()

#couse is-a salmon
cause = Salmon()

#harry is a halibut
harry = Halibut ()
