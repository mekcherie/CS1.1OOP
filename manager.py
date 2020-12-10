import random
from School import School
# inherting from class
class Manager(School): 
    def __init__(self, name, year, address,id):
      super().__init__(name, year, address, id)
      self.state_1 = ["Indiana", "California", "Texas"]
    
    def branch(self):
        l = random.choice(self.state_1)
        print(f"{self.name} is teaching at {l}")
        
        # overriding it
    def information(self):
        print(f"school name is {self.name} and branch is {random.choice(self.state_1)}")
 
abiy = Manager("abiy", 2, "3456 mlk blvd", 5425626)
abiy.branch()
abiy.information()
# private attribute double underscore 
# not to touch it outside of class 
