trial =0
while trial < 3:
    name= input('name: ')
    trial +=1
    if name != str ("David"):
        print("wrond username ")
    else :
        print("logged in successulfy")
        break # ends the loop when successful
else: print('locked')

