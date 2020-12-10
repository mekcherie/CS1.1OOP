from School import School
from manager import Manager
from  instructor import Instructor
from students import Students

businessschool = School("busines school", 2, "444 post st", 45646 )
abiy = Manager("abiy", 2, "3456 mlk blvd", 5425626)
jacob = Instructor("jacob", 2, "Assistant", "555 post st", 5425626, "business instructor", "Python")
jacob = Students("jacob", 20, "male", ["CS", "FEW", "BEW"])
businessschool.get_id()
businessschool.information()
