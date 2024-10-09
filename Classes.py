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
my_dog = Dog("Buddy", 3)

# Accessing attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3

# Calling methods
my_dog.bark()  # Output: Buddy says woof!
print(my_dog.get_human_years())  # Output: 21
