# Use append() to add Jupiter and Saturn at the end of the list.
# Use the extend() method to add another list of the last two 
# planets in our solar system to the end of the list.
# Use insert() to add Earth, and Venus in the correct order.
# Use append() again to add Pluto to the end of the list.
# Now that all the planets are in the list, slice the list in 
# order to get the rocky planets into a new list called rocky_planets.
# Being good amateur astronomers, we know that Pluto is now a dwarf planet, 
# so use the del operation to remove it from the end of planet_list.

planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
del planet_list[8]
rocky_planets = planet_list[0:4]
del planet_list[0:4]
# print(rocky_planets)
# print(planet_list)

# Create another list containing tuples. Each tuple will hold the name of a 
# spacecraft that we have launched, and the names of the planet(s) that it 
# has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
# Iterate over your list of planets, and inside that loop, iterate over the 
# list of tuples. Print, for each planet, which sattelites have visited.

final_frontiering = [("Hiten Probe", "Moon"), ("Cassini-Huygens", "Saturn", "Titan"), ("Mars Pathfinder", "Mars")]

all_planets_together = list()
all_planets_together.extend(planet_list)
all_planets_together.extend(rocky_planets)
print(all_planets_together)

for planet in all_planets_together:
	print(planet)
	for craft in final_frontiering:
		if planet in craft:
			to_print = ["Crafts that have been on above celestial bod:" + "craft"]
			print(craft)
			print(to_print)

