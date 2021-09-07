# OOP tutorial


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass


# Procedural, not object-oriented style


def create_animal(animal, animalName):
    animal.name = animalName
    print("Animal name is", animal.name)


def create_mammal(mammal, name, species, drinksMilk):
    create_animal(mammal, name)  # call the super constructor of the parent class
    # this line is analogous to super().__init__()
    mammal.drinksMilk = drinksMilk
    mammal.species = species
    print("I'm", mammal.name, mammal.species)
    print("Does", mammal.name, mammal.species, "drink milk?")
    if mammal.drinksMilk:
        print("Yes,", mammal.name, mammal.species, "drinks milk")
    else:
        print("No,", mammal.name, mammal.species, "doesn't drink milk.")


def create_dog(dog, name):
    create_mammal(dog, name, "dog", True)
    dog.woof = "I am a dog"
    print(name, "says: ", dog.woof)


animal = Animal()  # create a new empty object of type Animal
# the object is empty because there is no constructor
create_animal(animal, "Jerry")  # fill the object with data of animal

mammal = Mammal()
create_mammal(mammal, "Tom", "cat", True)

dog = Dog()
create_dog(dog, "Wolf")

mammal1 = Mammal()
create_mammal(mammal1, "Peppa", "Pig", True)
