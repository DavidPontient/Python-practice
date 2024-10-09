#First exercise :Print the Sum of a Current Number and a Previous number
# previous_num=0
# print("Printing current and previous number sum in a range(10)")
# for current_num in range(10):
#     totalsum= previous_num+current_num
#     print("Current Number "+str(current_num)+" Previous Number "+str(previous_num)+" Sum: "+str(totalsum))
#     previous_num=current_num

#Second Exercise :Print characters present at an even index number
# string=input("Input string: ")
# print(f"Orginal String is {string}")
# print("Printing only even index chars")
# for i in range(0, len(string), 2):
#     print(string[i])

#Third Exercise :Remove first n characters from a string
# string="Helloworld"
# n=input("number of letters to remove: ")
# for i in range(int(n),len(string)):
#     print(string[i],end="") #i added end="" for the letters to be displayed on one line

#Fourth Exercise : Check if the first and last numbers of a list are the same
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# numy1= numbers_y[0]
# numy2= numbers_y[-1]
# numx1= numbers_x[0]
# numx2= numbers_x[-1]
# print(f"Given list: {numbers_x}")
# if numx1 == numx2:
#     print("result is True")
# else:
#     print("result is False")

# print()#my way of putting space in the results lol

# print(f"Given list: {numbers_y}")
# if numy1 == numy2:
#     print("result is True")
# else:
#     print("result is False")

#Fifth Exercise: Display numbers divisible by 5
# num_list=[10, 20, 33, 46, 55]
# print(f"Given list is {num_list}")
# print("Divisible by 5")
# for i in num_list:
#     if i % 5 == 0: #if i/5: always evaluates to True because it checks if division is possible, which is valid for any number instead i used i % 5 ==0 which will check if theres any remainder if its zero then its divisable by 5
#      print(i)      

#Sixth Exercise : Find the number of times a word comes up.
# str_x ="Emma is good developer. Emma is a writer "
# count_emma=str_x.count("Emma")
# print(count_emma)

#Seventh Exercise : Print the following pattern
"""1
   22
   333
   4444
   55555
"""
# for i in range(6):
#     for t in range(i):
#       print(i,end=" ")
#     print("\n")

#Eight exercise : check if the number is the same when reversed eg 141 is 141 when reversed. 
# t= "Hello"
# treversed= t[::-1] # this is reversing for strings too
# print(treversed)

# num= input ("number: ")
# revnum=num[::-1]
# print(f"original number {num}")
# if str(num) == str (revnum):
#     print("Yes. given number is palindrome number")
# else:
#     print("No. given number is not palindrome number")

#Nineth Exercise: Merge two lists using the following condition
"""
Given two lists of numbers, write a Python code to create a new list such that the latest list 
should contain odd numbers from the first list and even numbers from the second list.
"""
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# t=[]
# x=[]

# for i in list1:
#  if i % 2 != 0: 
#       t.append(i) 
# for d in list2:
#     if d % 2 == 0:
#        x.append(d)
# print(f"result list: {t+x}")

#Tenth Exercise: Get each digit from a number in the reverse order. there must be space in each digit

# num= input("Number: ")
# revnum= num[::-1]
# spaced= " ".join(revnum)
# print(spaced)

#Eleventh Execise: Calculate income tax for the given income by adhering to the rules below
"""
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:
For example, suppose the income is 45000, and the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000.
"""
    
# f=10000*0
# n=10000*(10/100)
# income= input("income: $")
# t= int(income)-20000
# tax= t*(20/100)
# totaltax=f+n+tax
# print("$",totaltax)

#Twelvth Exercise: Print multiplication table from 1 to 10
# for i in range(1, 11):  # Loop through rows (1 to 10)
#     for j in range(1, 11):  # Loop through columns (1 to 10)
#         # Print the product, formatted with spaces
#         print(f"{i * j:2}", end=" ")  # `:2` ensures proper spacing for alignment
#     print()  # Move to the next line after each row

#Thirteenth Exercise: Print a downward half-pyramid pattern of stars
# num=[5,4,3,2,1]
# for i in num:
#     print(i*"*")

#Fourteenth Exercise: Get an int value of base raises to the power of exponent
#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def is used to defines a function 
base=input("base: ")
exp= input("exponent: ")
def exponent(base, exp):
    return int(base)**int(exp)
if int(exp)<0:
   print(f"{base} raises to the power of {exp}: 1 i.e. ({base}**-1= 1)")
else:
   output=exponent(int(base),int(exp))
   ie=" * ".join([base] * int(exp)) #generate the multiplication string for the exponentiation process
   print(f"{base} raises to the power of {exp}: {output} i.e. ({ie}= {output})")

    
 

