class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade  

    def gpa(self):
        return (self.grade*100)/8



grades=int(input("grades: "))
student= Student("David",grades)


print(f"The student {student.name} got {student.grade}, gpa= {student.gpa()}")
