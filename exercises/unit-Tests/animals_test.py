# Write test cases to verify the I/O of the following methods of Animal and Dog.

# x In the test class' setUpClass() method, create an instance of Animal and Dog.

# Animal object has the correct name property.

# Set a species and verify that the object property of species has the correct value.

# Invoking the walk() method set the correct speed on the both objects.

# The animal object is an instance of Animal.

# The dog object is an instance of Dog.


# Read the Test Discovery section of the Python docs. It explains how you can run all tests inside a directory. This allows you to split your unit test suite into many, smaller, more maintainable modules, and the use a pattern matcher to find tests in all matching files.

# python -m unittest discover -s . -p "Test*.py" -v

import unitest

from animals import Animal

class TestAnimalMethods(unittest.TestCase):

    # def setUp(self):
    #     self.Animal = Animal()

    def test_get_name(self):
    """Returns the animal's name"""
        self.assertEqual(Animal.get_name("Jerry"), "Jerry")

    def test_set_species(self):
    """Sets the species of the animal"""
        self.assertEqual(Animal.get_set_species("Sapiens"), "Sapiens")

    def test_walk(self):
    """Sets the speed of the animal"""
        self.assertEqual(Animal.walk())



scooby = Dog()
chipmunk = Animal("Chipmunk", "Tamiina", 30, 4)

class TestCalculationMethods(unittest.TestCase):

    def test_add(self):
        calculater = Calculator()
        self.assertEqual(calculator.add(2,2), 4)

    def test_subtract(self):
        calculater = Calculator()
        self.assertEqual(calculator.subtract(2,2), 0)

    def test_multiply(self):
        calculater = Calculator()
        self.assertEqual(calculator.multiply(2,3), 6)

    def test_divide(self):
        calculater = Calculator()
        self.assertEqual(calculator.divide(10, 5), 2)

