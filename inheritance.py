'''How does inheritance in Python enable the Manager and Developer classes to use and extend
   functionality from the Employee base class? Illustrate this with an example showing how 
   the Manager and Developer classes override methods and add new attributes.'''

# Base class
class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    
    def display_info(self):
        return f"Name: {self.name}, ID: {self.id_number}"
    
    def calculate_salary(self):
        raise NotImplementedError("Subclasses should implement this method.")

# Managers
class Manager(Employee):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department
    
    def display_info(self):
        return f"Manager - {super().display_info()}, Department: {self.department}"
    
    def calculate_salary(self):
        base_salary = 80000
        return base_salary

# Developers
class Developer(Employee):
    def __init__(self, name, id_number, programming_language):
        super().__init__(name, id_number)
        self.programming_language = programming_language
    
    def display_info(self):
        return f"Developer - {super().display_info()}, Programming Language: {self.programming_language}"
    
    def calculate_salary(self):
        base_salary = 60000
        return base_salary

manager = Manager(name="AJAY PRATAP RAI", id_number="M1710", department="Team Leader")
developer = Developer(name="Vishal Rai", id_number="D2000", programming_language="Python")

print(manager.display_info())
print(f"Manager Salary: ${manager.calculate_salary()}")  

print(developer.display_info())
print(f"Developer Salary: ${developer.calculate_salary()}")  
