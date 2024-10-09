#calculator
num1=int(input("number1: "))
num2=int(input("number2: "))
operator=input("Enter an operator( * + - / ^ ): ")
if operator == "*":
    print(num1*num2) 
elif operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator == "^":
    print(round(num1**num2,3)) #round to 3 decimal places
else:
    print(f"{operator}invalid operatol") 
    
