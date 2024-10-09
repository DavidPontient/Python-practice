#first method preserves the order
my_list=[1,2,2,3,4,5,5,6]
new_list=[]
# Use a for loop to go through each item in the 'numbers' list
for number in my_list:
  # Check if the number is not already in 'unique_numbers'
  if number not in new_list:
   new_list.append(number)# Add the number if it's unique
print(new_list)

# second is easier but order not guaranteed
new_list= list(set(my_list))
print(new_list)
