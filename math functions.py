#addiction
# number = input('eneter number ')
# print(type(number))
# addition = 1+ int(number) #remember to specify its an integer
# print (addition)
# sum_function =sum ([10,20,30]) #Python is used to add up all the elements in an iterable (like a list or tuple), not individual numbers passed as separate arguments.
# number = input('number ')
# print (sum_function + int (number) )
enternumbers = input('enter: ')
number_list = [int (num) for num in enternumbers.split()] #Converts each string into an integer and splits them
total_sum = sum(number_list)
print ('the total sum is '+str (total_sum))
num1= input ('first number: ')
multiply_sub= (int(num1)*2)-2
print (multiply_sub)
divid =10/2
print(divid)

