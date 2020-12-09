import random
from School import School
# inherting from class
class Manager(School): 
    address_1 = ["Indiana", "California", "Texas"]

    def __init__(self, name, year, position):
        self.name = name
        self.year = year
        self.position = position

    def location(self):
        l = random.choice(Manager.address_1)
        print(l)
        
        # # overriding it 
        # al = ("3456 mlk blvd")
        # print(f"my name is {self.name} I'm year {self.year} and I'm the school {self.position} and my address is {al}")
 
abiy = Manager("abiy", 5, "School Manager")
abiy.address_1()

# private attribute double underscore 
# not to touch it outside of class 
