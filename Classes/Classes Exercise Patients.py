class Patient:
    def __init__(self, id: int, name: str, age: int, gender: str, admission_date: str, condition: str):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition
    def get_details(self):
        return (f"Patient ID: {self.id}, Name: {self.name}, Age: {self.age}, "
                f"Gender: {self.gender}, Admission Date: {self.admission_date}, Condition: {self.condition}")
    
patient_1 = Patient(111, "David Kayumba", 19, "Male", "2024-11-24", "Recovering")
patient_2 = Patient(122, "Darwin Nunez", 23, "Male", "2024-10-30", "Critical")
patient_3 = Patient(133, "Mohammed Salah", 28, "Male", "2024-01-18", "Stable")
patient_4 = Patient(144, "Perla Kayumba", 10, "Female", "2024-04-13", "Stable")

patient_list=[patient_1, patient_2, patient_3, patient_4]
def count_patients(patient_list):
    return len(patient_list)
def list_patient_names(patient_list):
    for i in patient_list:
        print(i.name)
def print_patient_by_id(patient_list):
    id= int(input("ID: "))
    Found= False
    for i in patient_list:
        if id == i.id:
            print(i.get_details())
            Found= True
            break
    if not Found:
        print("Patient not found")
        
            
print_patient_by_id(patient_list)
