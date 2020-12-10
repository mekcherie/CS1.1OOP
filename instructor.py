import random
from School import School 
class Instructor(School): 
    def __init__(self, name, year, address, id, title, class_names, salary=3000):
        super().__init__(name, year, address, id)
        self._title = title
        self.class_names = class_names
        self._salary = salary
        self.assistant_names = []
        # print(f"my title is {self._title} getting paid around {self._salary} dollars")
        # init capaslock method lowercase
        # extend is creating 
    def assistant(self, assistant_names):
        self.assistant_names.extend(assistant_names)
        AB = self.class_names
        print(f" I'm teaching {AB}")

    def satsfiy_level(self, response):
        if response.lower() == "yes":
            print(f"{self.name} is very satsfied about the payment")
        else:
            print(f"{self.name} is sad")

joi = Instructor("joi", 2, "Assistant", "555 post st", 5425626, "CS instructor", "Python")
joi.assistant(["redi" "shash"])
joi.satsfiy_level("yes")

# SALARY CALCULATION


# protected bc we only want it to be accessed from a subclass






