class employees:
    def __init__(self,Fname,Lname,years):
        self.Fname= Fname
        self.Lname= Lname
        self.years= years
    def fullname(self):
        return self.Fname +" "+ self.Lname
    def salary(self):
        return self.years*100
    
fname=str(input("First name: "))
lname=str(input("last name: "))
First_employee= employees(fname, lname, 12)
print(f"Mister{First_employee.fullname()} worked {First_employee.years}, his current salary is {First_employee.salary()}")

