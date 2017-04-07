# Create an empty set named showroom.
# Add four of your favorite car model names to the set.
# Print the length of your set.
# Pick one of the items in your show room and add it to the set again.
# Print your showroom. Notice how there's still only one instance of that model in there.
# Using update(), add two more car models to your showroom with another set.
# You've sold one of your cars. Remove it from the set with the discard() method.

showroom = set()

showroom.add("Nova")
showroom.add("Chevelle")
showroom.add("Gremlin")
showroom.add("El Camino")

# print(showroom)	
# print(len(showroom))

showroom.add("El Camino")
#notice duplicate has not been added
# print(showroom)

new_cars = set()

new_cars.add("Firebird")
new_cars.add("Trans Am")

showroom.update(new_cars)

# print(showroom)

showroom.discard("Firebird")

# print(showroom)

junkyard = set()

junkyard.add("El Camino")
junkyard.add("Gremlin")
junkyard.add("La Sabre")
junkyard.add("Camaro")

cars_in_common = set.intersection(showroom, junkyard)
# print(cars_in_common)

new_showroom = showroom.union(junkyard)
new_showroom.discard("Trans Am")
print(new_showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old 
# cars has approached you about buying the entire inventory. In the new set, add some different cars, 
# but also add a few that are the same as in the showroom set.
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.