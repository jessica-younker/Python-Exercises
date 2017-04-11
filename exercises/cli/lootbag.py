import unittest
from lootbag import *

class TestBagOLoot(unittest.TestCase):

#decorater- @
#way to add funtionality to your class. here if you don't
 # add it, it will think SeUPClass is a method to test, so it 
 # @classmethod tells it to ignore it.

    @classmethod
    def setUpClass(self):
        self.self.bag = LootBag()

    def test_add_toy_bag(self):
        
        self.self.bag.test_add_to_bag("Ball", "Vincent")
        self.self.bag.list_toys_for_child("Vincent")
        vincents_toys = self.bag.list_toys_for_child("Vincent")

        #check if list first
        self.assertIsInstance(vincents_toys, list)
        self.assertIn("Ball", vincents_toys)

    def test_remove_toy_of_child(self):
        toy = "Slinky"
        self.bag.add_to_bag("Ball", "Vincent")
        self.bag.remove_toy_from_child("Ball", "Vincent")
        vincents_toys = self.bag.list_toys_for_child("Vincent")

        self.assertIn("Vincent", self.bag.get_kids())
        self.assertNotIn("Ball", vincents_toys)

    def test_list_of_good_kids(self):         
        toy = "Silly Putty"
        self.bag.add_to_bag(toy, "Vincent")
        good_kids = self.bag.get_kids()
        
        self.assertIsInstance(good_kids, list)
        self.assertIn("Vincent", good_kids)

    def test_toys_in_bag_for_specific_child(self):
        toy = "Slime"
        self.bag.add_to_bag(toy, "Vincent")
        vincents_toys = self.bag.list_toys_for_child("Vincent")

        self.assertIsInstance(vincents_toys, list)
        self.assertIn("Slime", vincents_toys)

    def test_child_toy_is_delivered(self):
        toy = "Pony"
        self.add_to_bag(toy, "Vincent")
        vincent = self.bag.get_single_child("Vincent")

        self.assertIsInstance(vincent, dict)
        self.assertFalse(vincent["delivered"])

        self.bag.deliver_toys_to_child("Vincent")
        self.assertTrue(vincent["delivered"])

# in command line python -m unittest discover -s . -p "Test*.py" -v
#-m sets context in python, takes argument 'discover'
# -s means "from what source"
#. = current directory
#-p, find files that match this pattern: 
