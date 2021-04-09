import unittest
from powers import powers_of_two, powers_of_three

class TestShift(unittest.TestCase):

    def test_powers_of_two(self):
        self.assertEqual(powers_of_two(0), [])
        self.assertEqual(powers_of_two(1), [1])
        self.assertEqual(powers_of_two(2), [1,2])
        self.assertEqual(powers_of_two(5), [1,2,4])
        self.assertEqual(powers_of_two(-1), [])

    def test_powers_of_three(self):
        self.assertEqual(powers_of_three(0), [])
        self.assertEqual(powers_of_three(1), [1])
        self.assertEqual(powers_of_three(3), [1,3])
        self.assertEqual(powers_of_three(33), [1,3,9,27])
        self.assertEqual(powers_of_three(-1), [])


if __name__ == '__main__':
    unittest.main()
