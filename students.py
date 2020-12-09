class Students:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    # instance method 
    def identity(self):
        print(f"I am a {self.age} years old {self.gender} student")

    def courses(self, subject):
        self.subject = "subject"
        print(f"and taking {self.age} {self.subject} courses")

jacob = Students(9, "male")
jacob.identity()
jacob.courses("business")