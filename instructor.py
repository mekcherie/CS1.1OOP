from School import School 
from manager import Manager
from students import Students
class Instructor(School): 
    def __init__(self, name, year, address, id, title, class_names, salary=3000):
        super().__init__(name, year, address, id)
        self._title = title # protected bc we only want it to be accessed from a subclass
        self.class_names = class_names
        self.__salary = salary  # private  
        self.assistant_names = []
        # extend is putting it all together in a list while in append it prints out one by one
    def assistant(self, assistant_names):
        self.assistant_names.extend(assistant_names)
        AB = self.class_names
        print(f" I'm a {AB}")

    def satsfiy_level(self, response):
        if response.lower() == "yes":
            print(f"{self.name} is very satsfied about the payment")
        else:
            print(f"{self.name} is sad about the payment")

jacob = Instructor("jacob", 2, "Assistant", "555 post st", 5425626, "business instructor")
jacob.assistant(["luke" "abiy"])
jacob.satsfiy_level("yes")


businessschool = School("busines school", 2, "444 post st", 45646 )
jacob = Instructor("jacob", 2, "Assistant", "555 post st", 5425626, "business instructor", "Python")
jacob = Students("jacob", 20, "male", ["CS", "FEW", "BEW"])


businessschool.get_id()
businessschool.information()

jacob.identity()
jacob.courses()









