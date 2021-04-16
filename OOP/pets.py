# Implement classes, test them with unit tests.

# The relationship is one owner to many pets, one owner can own many pets.
# One pet can belong to many owners. We will fix this later.
# Owner has a name attribute.
# Owner has a list of owned pets attribute.


class Owner:
    def __init__(self, name):
        self.person_name = name
        self.adopted_pets = []

    def adopt(self, pet):
        if pet not in self.adopted_pets:
            self.adopted_pets.append(pet)

    def abandon(self, pet):
        self.adopted_pets.remove(pet)

    def owns(self, pet):
        return pet in self.adopted_pets


class Pet:
    def __init__(self, name):
        self.pet_name = name


alice = Owner("Alice")
bob = Owner("Bob")
tom = Pet("Tom")
jerry = Pet("Jerry")
print(alice.owns(tom))  # False
print(alice.owns(jerry))  # False

alice.adopt(tom)
alice.adopt(jerry)

print(alice.owns(tom))  # True
print(alice.owns(jerry))  # True

alice.abandon(tom)
alice.abandon(jerry)

print(alice.owns(tom))  # False
print(alice.owns(jerry))  # False

bob.adopt(tom)
bob.adopt(jerry)
