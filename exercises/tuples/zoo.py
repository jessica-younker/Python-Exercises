# Create a tuple named zoo that contains your favorite animals.

# Find one of your animals using the .index(value) method on the tuple.

# Determine if an animal is in your tuple by using for value in tuple.

# Create a variable for each of the animals in your tuple with this cool feature of Python.

# # example
# (lizard, fox, mammoth) = zoo
# print(lizard)
# Convert your tuple into a list.

# Use extend() to add three more animals to your zoo.

# Convert the list back into a tuple.

zoo = ("zebra", "monkey", "manatee", "penguin", "lion", "gorilla")

print(zoo.index("zebra"))

possible_new_animals = ("snake", "manatee", "penguin", "guinea pig")

for possible_animal in possible_new_animals:
	if possible_animal in zoo:
		print("yes, animal in zoo")
	else:
		print("nope, don't have this one")

(zebra, monkey, manatee, penguin, lion, gorilla) = zoo
print(zebra)

zoo_list = list(zoo)
print(zoo_list)

zoo_list.extend(["puma", "gopher", "turtle"])

print(zoo_list)

zoo = tuple(zoo_list)
print(zoo)
