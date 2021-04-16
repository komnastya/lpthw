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
        if pet in self.adopted_pets:
            return False
        if pet.pet_owner != None:
            pet.pet_owner.abandon(pet)
        pet.pet_owner = self
        self.adopted_pets.append(pet)
        return True

    def abandon(self, pet):
        if pet not in self.adopted_pets:
            return False
        self.adopted_pets.remove(pet)
        pet.pet_owner = None
        return True

    def owns(self, pet):
        return pet in self.adopted_pets


class Pet:
    def __init__(self, name):
        self.pet_name = name
        self.pet_owner = None
