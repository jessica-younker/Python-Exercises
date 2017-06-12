# Write test cases to verify the I/O of the following methods of Animal and Dog.

# In the test class' setUpClass() method, create an instance of Animal and Dog.

# Animal object has the correct name property.

# Set a species and verify that the object property of species has the correct value.


# The animal object is an instance of Animal.

# The dog object is an instance of Dog.


# Read the Test Discovery section of the Python docs. It explains how you can run all tests inside a directory. This allows you to split your unit test suite into many, smaller, more maintainable modules, and the use a pattern matcher to find tests in all matching files.

# python -m unittest discover -s . -p "Test*.py" -v

import unittest

from animals import Animal, Dog

class TestAnimalMethods(unittest.TestCase):

    def setUpClass():
        critter = Animal()
        scooby = Dog(Animal)
        print(scooby)

    def setUp(self):
        self.animal = Animal(name="Jerry")

    def test_get_name(self):       
        self.assertEqual(self.animal.name, "Jerry")

    def test_set_species(self):
        self.animal.set_species("jeromus") 
        self.assertEqual(self.animal.species, "jeromus")
# Invoking the walk() method set the correct speed on the both objects.

    def test_walk(self):
        self.animal.set_legs(number_of_legs=6)
        self.animal.walk()
        self.assertAlmostEqual(self.animal.speed, .6)
        
        self.assertRaises(ValueError, self.animal.set_legs, number_of_legs=0)
        self.animal.walk()



if __name__ == '__main__':
    unittest.main()

