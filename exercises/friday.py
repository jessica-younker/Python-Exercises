#single inheritance/ is-a relationship
class Animal:
	#init method is not inherited. init runs w/ instance of a class (not on class definition)
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0

    def getName(self):
        return self.name

    def walk(self):
        print("Parent class walk method")
        self.speed = self.speed + (0.1 * self.legs)

    def setSpecies(self, species):
        self.species = species

    def getSpecies(self):
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "{} is a {}".format(self.name, self.species)

#you can leave out parentheses...or have it with object(python object) in thur
class IsWhiskered(object):
	def __init__(self):
		self.whiskers = True
		self.whiskers_count = 0

	def loseWhisker(self,count):
		self.whiskers_count -= count

class IsClawed:
	def __init__(self, retractable=False):
		self.claws = True
		self.claws_are_retractable = retractable


class Dog(Animal, IsWhiskered):
    def __init__(self, name):
    	#for dog to get properties of Animal (currently just has methods of Animal):
        Animal.__init__(self, name, "Dog")
        #with super don't need to pass 'self'
        super().__init__(name, "Dog")

    def walk(self):
        self.speed = self.speed + (0.2 * self.legs)


class Cat(Animal, IsWhiskered, IsClawed):
    def __init__(self, name):
    	#for dog to get properties of Animal, do class.__init__ (currently just has methods of Animal):
        Animal.__init__(self, name, "Cat")
        IsWhiskered.__init__(self)
        IsClawed.__init__(self, True)
        #super().__init__(self, name, "Dog")

    def walk(self):
        self.speed = self.speed + (0.25 * self.legs)


fido = Dog()
tommy = Animal("Tommy", "Tortoise")

#method overriding--override parent's method's behavior with specific set of logic in subclass

#super() refers to parent class. indicates a single inheritance