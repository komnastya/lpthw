import unittest

from pets import Owner, Pet


class TestPets(unittest.TestCase):
    def test_initially_not_onwed(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        self.assertFalse(owner.owns(pet))
        self.assertIsNone(pet.owner)

    def test_owner_adopts_an_orphat_pet(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        self.assertTrue(owner.adopt(pet))
        self.assertTrue(owner.owns(pet))
        self.assertIs(pet.owner, owner)

    def test_owner_adopts_a_pet_it_already_owns(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        self.assertTrue(owner.adopt(pet))
        self.assertFalse(owner.adopt(pet))
        self.assertTrue(owner.owns(pet))
        self.assertIs(pet.owner, owner)

    def test_owner_adopts_a_pet_owned_by_someone(self):
        alice = Owner("Alice")
        bob = Owner("Bob")
        pet = Pet("Tom")

        self.assertTrue(alice.adopt(pet))
        self.assertTrue(bob.adopt(pet))

        self.assertFalse(alice.owns(pet))
        self.assertTrue(bob.owns(pet))
        self.assertIs(pet.owner, bob)

    def test_owner_abandon_pet_it_owns(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        self.assertTrue(owner.adopt(pet))
        self.assertTrue(owner.abandon(pet))

        self.assertFalse(owner.owns(pet))
        self.assertIsNone(pet.owner)

    def test_owner_abandon_pet_it_does_not_own(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        self.assertFalse(owner.abandon(pet))

    def test_pet_gets_an_owner(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        pet.owner = owner

        self.assertTrue(owner.owns(pet))
        self.assertIs(pet.owner, owner)

    def test_pet_changes_an_owner(self):
        alice = Owner("Alice")
        bob = Owner("Bob")
        pet = Pet("Tom")

        pet.owner = alice

        self.assertTrue(alice.owns(pet))
        self.assertFalse(bob.owns(pet))
        self.assertIs(pet.owner, alice)

        pet.owner = bob

        self.assertFalse(alice.owns(pet))
        self.assertTrue(bob.owns(pet))
        self.assertIs(pet.owner, bob)

    def test_pet_loses_an_owner(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        pet.owner = owner

        self.assertTrue(owner.owns(pet))
        self.assertIs(pet.owner, owner)

        pet.owner = None

        self.assertFalse(owner.owns(pet))
        self.assertIsNone(pet.owner)

    def test_pet_changes_its_owner_to_the_same_owner(self):
        owner = Owner("Alice")
        pet = Pet("Tom")

        pet.owner = owner
        pet.owner = owner

        self.assertTrue(owner.owns(pet))
        self.assertIs(pet.owner, owner)


if __name__ == "__main__":
    unittest.main()
