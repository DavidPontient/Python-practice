#Second part of the menu
fruits={
    "mango":     12,
    "pineapple": 13,
    "Apples":    20
        
    }
input("Username: ")
input("Location: ")
print("What Fruits you would like to purchase ?")
for fruit, num_of_fruits in fruits.items():
    print(fruit,num_of_fruits)
choice= input("Fruits: ")
if choice in fruits.keys():
    print("Please enter the amount: ")
    amount = input()
    if amount.isdigit() and 0 < int(amount) <= fruits[choice]: # checks if the amount is more than zero and bwteen the number of fruits in stock
        print(f"You have purchased {amount} {choice}(s).")
    else:
        print("Invalid amount or not enough stock")
else:
    print("OOps looks like we dont have that fruit")
#first part of the menu
print("Welcome to the fruit app")
print("Would you like to purchase fruits ? type yes or no")
answer=input()
trial=2
while trial> 0 :
    if answer.lower() != "no" and answer.lower() != "yes":
        print("Invalid answer! try again")
        answer=input()
        trial -= 1
    elif answer.lower() == "no":
        print("Thank You for visiting our app")
        break
    else:
        print("Continue with the purchase")
        break
    if trial == 0 and answer.lower() not in ["yes", "no"]:
        print("No more attempts left. Please restart the app.")