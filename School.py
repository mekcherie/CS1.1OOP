import random
class School:
    badge_numbers = [9786, 5864, 2849]
    school_address = ("3566 post road")

    def __init__(self, name, year):
        self.name= name 
        self.year= year 

    @classmethod 
    def Employee (cls):
        bn = random.choice (cls.badge_numbers)
        print(f"my badge number is {bn}")

    def rn (self):
        al = School.school_address
        print(f"my name is {self.name} I'm year {self.year} and my address is {al}")


# luke = School("Luke", 2)
# luke.rn()
# jacob = School("jacob", 25) 
# jacob.Employee()





# we created a class
# the badge number is a class attributes(adding class attributes)
# instance attributes, parameteres 
#def
# creating an attribute and assigning it 
# creating class method 
# passing arguments 
# initilized it/ calling it 
 







