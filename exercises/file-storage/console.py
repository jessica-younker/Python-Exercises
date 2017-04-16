# Create a single class that implements all functionality.
# Create a method for reading the car makes file.
# Create a method for reading the car models file.
# Create a method that invokes the previous two methods and 
# generates a dictionary.
# The dictionary keys will be the make names.
# The value for each key will be a list of model names.
# {
#     "Toyota": ["Camry"],
#     ...
# }/
import sys

class Carlot(object):

    def __init__(self):
        self.makes_list = []
        self.models_list = []
        self.create_car_dict = {}

    def read_makes(self):
        with open("car-makes.txt", "r") as car_makes:
            for line in car_makes:
                self.makes_list.append(line.replace("\n", ""))
        print(self.makes_list)
    
    def read_models(self):
        with open("car-models.txt", "r") as car_models:
            for line in car_models:
                self.models_list.append(line.replace("\n", "").split("="))
        print(self.models_list)
     
    def build_car_dictionary(self):
        for make in self.makes_list:
            make_list = []
            for model in self.models_list:
                if make[0]==model[0]:
                    make_list.append(model[1])
            self.create_car_dict[make]=make_list
        print(self.create_car_dict)
                  

run = Carlot()
run.read_makes()
run.read_models()
run.build_car_dictionary()

