# secretnum = 5
# number= input('Geuss: ') # initial number 
# while secretnum != int (number): # loop everything bellow if secretnum not equal to number
#     number = int(input("Geuss: ")) #keeps on asking number when not found, though different var it must be the same as the number varible in the loop
# print ("congratulation")
secretnum = 5
guesscount = 0
guesslimit = 3
while guesscount < guesslimit : #can use both not equals or <
    guess= int(input ("Geuss "))# Prompt the user for a guess
    guesscount +=1 # incriment the guess attempts 
#     if guess == secretnum : 
#         print("You win ")      
#         break # Exit loop if geuss ==secretnum
# else:# This block executes only if the while loop is not broken
#     print('You Loose') 

    

