limit=3
gcount=0
guess=3
while gcount < limit:
    num=int(input("Guess number range 1-4: "))
    if num != guess:
        print("try again ")
        gcount+=1
    else:
        print("correct")
        break
else:print("youve reached guess limit")    
