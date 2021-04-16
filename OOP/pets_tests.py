import unittest
from pets import Owner, Pet

class TestPets(unittest.TestCase):
    def test_owns(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        self.assertFalse(owner.owns(pet))

        owner.adopt(pet)
        self.assertTrue(owner.owns(pet))

        owner.abandon(pet)
        self.assertFalse(owner.owns(pet))


    def test_adopted_by_many(self):
        owner0 = Owner("Alice")
        owner1 = Owner('Bob')
        pet0 = Pet("Tom")
        pet1 = Pet("Jerry")

        owner0.adopt(pet0)
        owner0.adopt(pet1)
        owner1.adopt(pet0)

        self.assertTrue(owner0.owns(pet0))
        self.assertTrue(owner0.owns(pet0))
        self.assertTrue(owner1.owns(pet0))


    def test_abandon(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        owner.adopt(pet)
        owner.abandon(pet)

        self.assertFalse(owner.owns(pet))


if __name__ == '__main__':
    unittest.main()
