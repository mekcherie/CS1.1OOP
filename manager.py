from School import School
# inherting from class
class Manager(School): 
    def __init__(self, name, year, postiion):
        self.name = name
        self.year = year
        self.postiion = postiion
        # print(f"my name is {self.name} and my age is {self.a} I work as a {self.postiion}")


        al = ("3456 mlk blvd")
        print(f"my name is {self.name} I'm year is {self.year} and my address is {al}")
 
jacob =Manager("jacob", 25, "School") 
jacob.managerrn()
# mark = Manager("mark", 30, "Manager")

