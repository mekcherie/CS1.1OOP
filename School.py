import random
# created class 1
class School():
    # we gave a badge number which is a class attribute 
    badge_numbers = [9786534, 38647203, 284936389]
    school_address = ("3566 post road")
    # add class attribute 
    # instance attribute , parameteres 
    def __init__(self, name, year):
        # the indentation is important because its telling
        #  python that it belongs to the  Employee class. 
        # creating an attribute and assignign it
        self.name= name 
        self.year= year 
        # i created class method 
    @classmethod 
    def Id (cls):
        bn = random.choice (cls.badge_numbers)
        print(bn)

    def rn (self):
        al = School.school_address
        print(f"my name is {self.name} I'm year is {self.year} and my address is {al}")
 
# passing arguments 
mark = School("mark", 30)
jacob = School("jacob", 25) 
# print(Employee.badge_number)
# initilized it/ calling it 
mark.rn()
jacob.rn()






