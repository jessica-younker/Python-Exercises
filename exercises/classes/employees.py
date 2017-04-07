# # Create a class that contains information about employees of a 
# company and define methods to get/set employee name, job title, 
# and start date.
class Employee:
	def__init__(self, name, title, start_date):
		self.name = name
		self.title = title
		self.start_date = start_date

	def get_name(self):
		"""Returns the name of the company"""
		return self.name
       
    def get_title(self):
    	return self.title


    def get_start_date(self):
    	return self.start_date

	# Copy this Company class into your module.
class Company(object):
    """This represents a company in which people work"""
    def __init__(self, name):
        self.name = name

        self.employees = set()
       
    def get_name(self):
        """Returns the name of the company"""
        return self.name

    # Add the remaining methods to fill the requirements above
 
	# Consider the concept of aggregation, and modify the Company 
	# class so that you assign employees to a company.
	# Create a company, and three employees, and then assign the
	# employees to the company.
	The_Company_Company = Company("The Company Company")

	marvin = Employee("Marvin", "Mail Room Head", "10 April 2010")
	shirley = Employee("Shirley", "Lunch Lady", "10 April 2010")
	bonnie = Employee("Bonnie", "Custodian", "10 April 2010")

	 
	The_Company_Company.employees.add(marvin)
	The_Company_Company.employees.add(shirley)
	The_Company_Company.employees.add(bonnie)

	