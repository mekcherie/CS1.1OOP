# created class 1
class country(): 
    def __init__(self, state,city, county,district):
        self._state= state
        self.__city= city 
        self.county=  county
        self.district= district

        print(f"my state is {self._state} and my city is in {self.__city} but my county is {self.county}")
# inheriting ome class 
mek = country("califronia", "san jose","santa clara", '')