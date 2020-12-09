import random
from School import School 
class Instructor(School): 
    class_given = ["maths"]
    def __init__(self, name, year, title, salary):
        super().__init__(name, year)
        self._title = title
        self._salary = salary
        print(f"my title is {self._title} getting paid around {self._salary} dollars")

    def level(self, status):
        self.status = status 
        AB = (Instructor.class_given)
        print(f" I'm teaching {AB}")

    def satsfied(self):
        print(f"The instrictor is very satsfied")

jacob = Instructor("jacob", 9, "Assistant", 3000)
jacob.level(2)
jacob.satsfied()




# protected bc we only want it to be accessed from a subclass
#  one underscore 





