class Students:
    def __init__(self, student_name, age, gender, subject):
        self.__student_name = student_name  #private you can not touch it from outside the class, the result will be Attribute Error
        self.__age = age
        self.__gender = gender
        self.__subject = subject
        
    def identity(self):
        print(f"I am a {self.__age} years old {self.__gender} student")

    def courses(self):
        for i in range(len(self.__subject)):
            print(f"course -- {self.__subject[i]}")

jacob = Students("jacob", 20, "male", ["CS", "FEW", "BEW"])
jacob.identity()
jacob.courses()
