# refactor using decorators?

import random

class Department(object):
    """Parent class for all departments"""
    def __init__(self, name, manager, employee_count):
        self.name = name
        self.manager = manager
        self.employee_count = employee_count
        self.budget = 20000

    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return ""
            # print("Get_name error")??

    def set_name(self, val):
        if isinstance(val, str):
            raise TypeError('Please provide a string value for the department name')

        if val is not "" and len(val) > 1:
            self.__name = val
        else:
            raise ValueError("Please provide a department name")

    def get_manager(self):
        try:
            return self.__manager
        except AttributeError:
            return ""

    def set_manager(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the manager name')

        if val is not "" and len(val) > 5:
            self.__manager = val
        else:
            raise ValueError("Please provide a manager name")

    def add_policy(self, policy_name, policy_text):
        """Adds a policy, as a tuple, to the set of policies

        Arguments:
        policy_name (string)
        policy_text (string)
        """ 
        self.policies.add(policy_name, policy_text)
        self.policies = set()

    def get_policy(self, policy_name):
        try:
            return self.__policy
        except AttributeError:
            return ""

    def get_employee_count(self):
        try:
            return self.__employee_count
        except AttributeError:
            return ""

    def set_employee_count(self, val):
        if not isinstance(val, int):
            raise TypeError('Please provide an integer to count employee')

    def meet(self, manager, date, time):
        print("Everyone meet in {}'s office".format(self.manager))

    def get_budget(self):
        return self.budget

# class HumanResources(Employee, FullTime):
#   """Describes human resources employees"""

#   def __init__(self, first_name, last_name):
#     super().__init__(first_name, last_name) # super is Employee
#     FullTime.__init__(self)
class HumanResources(Department):
    """Class for representing Human Resources department
        Methods: __init__, add_policy, get_policy, etc."""
    def __init__(self, name, manager, employee_count):
        super().__init__(name, manager, employee_count)
    
        self.budget = super().get_budget() - 1000
    
    def hire_person(self, name):
        print("you have hired that person")

    def fire_person(self, name):
        print("you have fired that person")

    def meet(self, date, time):
        print("Everyone meet in conference room")
   
class Marketing(Department):
    """Class for representing Marketing department
        Methods: __init__, add_policy, get_policy, etc."""
    def __init__(self, name, manager, employee_count):
        super().__init__(name, manager, employee_count)

        self.budget = super().get_budget() - 10000

    def design_brand(self):
        print("brand")
        
    def meet(self, date, time):
        print("Everyone meet in breakroom")

class Manufacturing(Department):
    """Class for representing Manufacturing department
        Methods: __init__, add_policy, get_policy, etc."""
    def __init__(self, name, manager, employee_count):
        super().__init__(name, manager, employee_count)

        self.budget = super().get_budget() - 1200
       
    def source_materials(self):
        print("raw materials list")

    def meet(self, date, time):
        print("Everyone meet in parkinglot")

class Accounting(Department):
    """Class for representing Accounting department
        Methods: __init__, add_policy, get_policy, etc."""
    def __init__(self, name, manager, employee_count):
        super().__init__(name, manager, employee_count)

        self.budget = super().get_budget() - 3000
     
    def approve_budget(self): 
        print("budget approved")     

    def meet(self, date, time):
        print("Everyone meet in conference room B")


class Employee(object):
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
        
    def eat(self, food=None, companions=None):
      
        s = "{} {} ".format(self.firstname, self.lastname)
        if food:
            s += "ate " + food + " at the office"
        else:            
            possible_restaurants_list = ["mj's", "gaby's", "larry's", "stinky's"]
            restaurant = random.choice(possible_restaurants_list)
            s += "ate at " + restaurant
        
        if companions:    
            var_companions = [c.firstname for c in companions]
            strung_companions = ", ".join(var_companions)
            s += " with " + strung_companions
        else:
            s += " all alone"
        
        return s


    

# class Full_Time:
#     def __init__(self):
#         self.hours_per_week = 40

# class Part_Time:
#     def __init__(self):
#         self.hours_per_week = 24


# class HumanResourcesAdministrator(Employee):
#     pass


# class HeatherMcGee(HumanResourcesAdministrator, Full_Time):
#     pass


# class MC(HumanResourcesAdministrator, Part_Time):
#     pass



if __name__ == '__main__':
       
    hr_dept = HumanResources("HumanResources", "Walter Sobcek", 21)
    mktg_dept = Marketing("Marketing", "Maude Lebowski", 17)
    mfkg_dept = Manufacturing("Manufacturing", "Jackie Treehorn", 44)
    acct_dept = Accounting("Accounting", "Bunny Lebowski", 5)  

    Sam = Employee("Sam", "Samuelz")
    Bert = Employee("Bert", "Samuelz")
    Dean = Employee("Dean", "Samuelz")
    Alice = Employee("Alice", "Samuelz")



    
    # acct_dept.add_policy("Policy1", "the first policy") 
    # print(acct_dept.policies)
    print(acct_dept.budget)
    print(hr_dept.manager)
    print(mktg_dept.manager)
    print(mfkg_dept.name)
    print(acct_dept.name)
    print(Sam.eat())
    print(Sam.eat(food="sangawich"))
    print(Sam.eat(companions=[Bert, Dean, Alice]))
    print(Sam.eat("pizza",  [Bert, Dean, Alice]))
