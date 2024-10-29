#User Log in details
u_name= "david"
address= "kigali"
def login():
    username= input("Username: ")
    if username == u_name:
        location= input("Location: ")
        if location == address:
            return True
        else:
            print("wrong address")
            return False
    else:
        print("invalid user")
        return False