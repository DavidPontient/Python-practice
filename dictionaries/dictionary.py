# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "sex" : "Male"
}

# Accessing values using keys
print(student["name"])  # Output: John Doe
print(student["age"])   # Output: 20

# Adding a new key-value pair
student["graduation_year"] = 2024

# Modifying an existing value
student["age"] = 21

# Accessing all keys
print(student.keys())  # Output: dict_keys(['name', 'age', 'major', 'graduation_year'])

# Accessing all values
print(student.values())  # Output: dict_values(['John Doe', 21, 'Computer Science', 2024])

# Accessing all key-value pairs
print(student.items())  # Output: dict_items([('name', 'John Doe'), ('age', 21), ('major', 'Computer Science'), ('graduation_year', 2024)])

# Deleting a key-value pair
del student["major"]

# Checking if a key exists
if "name" in student:
    print("Name exists in the dictionary")

