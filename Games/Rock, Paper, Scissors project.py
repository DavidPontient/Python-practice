#Rock Paper Scissors
R="Rock"
P="Paper"
S="Scissor"
import random
choices=["Rock","Paper","Scissor"]
pc_choice=random.choice(choices)
pc_Lchoice= pc_choice.lower()

p1_choice= input("Enter Rock Paper or Scissor ").lower()

print("pc choice:",pc_choice)
if p1_choice == pc_Lchoice:
    print("Tie: try again")
elif p1_choice == R.lower() and pc_Lchoice == S.lower():
    print("P1 win")
elif p1_choice == P.lower() and pc_Lchoice == R.lower():
    print("P1 win")
elif p1_choice == S.lower() and pc_Lchoice == P.lower():
    print("P1 win")
elif p1_choice == R.lower() and pc_Lchoice == P.lower():
    print("Pc win")
elif p1_choice == P.lower() and pc_Lchoice == S.lower():
    print("Pc win")
elif p1_choice == S.lower() and pc_Lchoice == R.lower():
    print("Pc win")   
else:
    print("Invalid Input")
