class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute to store the dog's name
        self.age = age    # Attribute to store the dog's age

    def bark(self):
        print(f"{self.name} says woof!")

    def get_human_years(self):
        # Convert dog's age to human years (1 dog year = 7 human years)
        return self.age * 7
    
   
        
        

# Creating an instance (object) of the Dog class
first_dog = Dog("Buddy", 3)
second_dog= Dog("mika", 4)

# Accessing attributes
print(f"My dogs name is {second_dog.name}")  # Output: Buddy   

# Calling methods
second_dog.bark()  # Output: Buddy says woof!
print(f"{second_dog.name}'s age is {second_dog.age}, in Human years its {second_dog.get_human_years()}")  # Output: 21
