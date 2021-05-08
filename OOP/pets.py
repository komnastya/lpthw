import unittest


class Owner:
    def __init__(self, name):
        self.person_name = name
        self._adopted_pets = []

    def adopt(self, pet):
        if self.owns(pet):
            return False
        if pet.owner != None:
            pet.owner.abandon(pet)
        self._adopted_pets.append(pet)
        pet.owner = self
        return True

    def abandon(self, pet):
        if not self.owns(pet):
            return False
        self._adopted_pets.remove(pet)
        pet.owner = None
        return True

    def owns(self, pet):
        return pet in self._adopted_pets and pet.owner is self

    def _is_consistent(self):
        for pet in self._adopted_pets:
            assert pet._pet_owner is self


class Pet:
    def __init__(self, name):
        self.pet_name = name
        self._pet_owner = None

    @property
    def owner(self):
        return self._pet_owner

    @owner.setter
    def owner(self, owner):
        if self._pet_owner == owner:
            return False
        if self._pet_owner is not None:
            self._pet_owner._adopted_pets.remove(self)
        self._pet_owner = owner
        if self._pet_owner is not None:
            self._pet_owner._adopted_pets.append(self)
        return True

    def _is_consistent(self):
        assert self._pet_owner.owns(self)
