import random
class School:

    # 2 instance attributecreated 
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


makeschool = School("makeschool", 2, "555 post st", 45646 )
makeschool.information()
makeschool.get_id()












# we created a class
# the badge number is a class attributes(adding class attributes)
# instance attributes, parameteres 
#def
# creating an attribute and assigning it 
# creating class method 
# passing arguments 
# initilized it/ calling it 
 







