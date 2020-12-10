import random
class School:
      # init capaslock method lowercase
    def __init__(self, name, year, address, id):
    # class attributes 
        self.name= name 
        self.year= year 
        self.address = address
        self.id = id
        
    # 2 methods created 
    def get_id(self):
        bn = self.id
        print(f"school Id is {bn}")

    def information(self):
        print(f"{self.name} has been around {self.year} years and the address is {self.address}")

# initilized it/ calling it 
businessschool = School("busines school", 2, "444 post st", 45646 )
businessschool.information()
businessschool.get_id()

 







