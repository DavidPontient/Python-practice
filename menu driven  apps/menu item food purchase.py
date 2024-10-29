#food app
from userlogin import login, u_name
fruits={
    "mango":     12,
    "pineapple": 13,
    "Apples":    20
        
        }

def intro():
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
            User()
            break
        if trial == 0 and answer.lower() not in ["yes", "no"]:
            print("No more attempts left. Please restart the app.")


def User():
    if login():
        print("What Fruits you would like to purchase ?")
        for fruit, num_of_fruits in fruits.items():
            print(fruit,num_of_fruits)
            
        choice= input("Fruits: ")
        if choice in fruits.keys(): # checks if the fruit is in the fruit key(fruits we have), remember key: values in hashmaps/dictionaries
            print("Please enter the amount: ")
            amount = input()
            if amount.isdigit() and 0 < int(amount) <= fruits[choice]: # checks if the amount is more than zero and bwteen the number of fruits in stock
                print(f"{u_name} has purchased {amount} {choice}(s).")
            else:
                print("Invalid amount or not enough stock")
        else:
            print("OOps looks like we dont have that fruit")


intro()
