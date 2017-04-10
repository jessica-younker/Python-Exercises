# Using the random module and the range method, generate a list 
# of 20 random numbers between 0 and 49.
	
	# import random

	# random_numbers = [...insert awesome code here...]
	# print(random_numbers)

import random

random_numbers = random.sample(range(50), k=50)
print(random_numbers)

randoms_squared = [num**2 for num in random_numbers]
print(randoms_squared)

# With the resulting list, use a list comprehension to build a new 
# list that contains each number squared. For example, if the original 
# list is [2, 5], the final list will be [4, 25].