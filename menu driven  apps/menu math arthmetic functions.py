choices="""
1.addition
2.subtraction
3.multiplication
4.division
"""
def addition():
    num_1=int(input("First number: "))
    num_2=int(input("Second number: "))
    print()
    print("PERFORMING ADDITION")
    print(f"{num_1}+{num_2}")
    return num_1 + num_2
def subtraction():
    num_1=int(input("First number: "))
    num_2=int(input("Second number: "))
    print()
    print("PERFORMING SUBTRACTION")
    print(f"{num_1}-{num_2}")
    return num_1 - num_2
def multiplication():
    num_1=int(input("First number: "))
    num_2=int(input("Second number: "))
    print()
    print("PERFORMING MULTIPLICATION")
    print(f"{num_1}x{num_2}")
    return num_1 * num_2
def division():
    num_1=int(input("First number: "))
    num_2=int(input("Second number: "))
    print()
    print("PERFORMING DIVISION")
    print(f"{num_1}/{num_2}")
    return num_1/num_2

print(choices)
select=int(input("Select any  arithmetic option: "))
if select == 1:
    print(addition())
elif select == 2:
    print(subtraction())
elif select == 3:
    print(multiplication())
elif select == 4:
    print(division())  
else:
    print("Invalid choice")  


    



