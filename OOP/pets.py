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
        if pet not in self.adopted_pets and pet.pet_owner == None:
            self.adopted_pets.append(pet)
            pet.pet_owner = self
            return True
        else:
            return False

    def abandon(self, pet):
        self.adopted_pets.remove(pet)
        pet.pet_owner = None

    def owns(self, pet):
        return pet in self.adopted_pets


class Pet:
    def __init__(self, name):
        self.pet_name = name
        self.pet_owner = None
