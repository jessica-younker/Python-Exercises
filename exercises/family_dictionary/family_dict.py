# Define a dictionary that contains information about several members of your family. 
# Use the following example as a template.

my_family = {
    'father': {
        'name': 'Bruce',
        'age': 62
    },
    'mother': {
        'name': 'Mary',
        'age': 65
    },
    'oldest_brother': {
        'name': 'Matt',
        'age': 39
    },
    'weird_brother': {
        'name': 'Paul',
        'age': 37
    },
    'little_brother': {
        'name': 'Benji',
        'age': 30
    },
}
# Using a dictionary comprehension, produce output that looks like the following example:
# 	Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value) 

family_members = {my_family[k]['name'] + " is my " + k.replace('_', ' ') + " and is " + str(my_family[k]['age']) + " years old" for (k,v) in my_family.items()}

print(family_members)
