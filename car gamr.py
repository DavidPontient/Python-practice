# car game should include help to preview the controls, start, stop, quit and "i dont understand" if an uknown value entered" 
help_text = '''start - to stat the car
stop - to stop the car
quit- to exit 
'''
start = 'The car has started'
stop = 'The car has stoped'
quit_text = 'Process terminated'

while True: #Loop to continuously ask for user input until 'quit' is entered
    d = input("play: ").strip().lower()
    if d != 'help' and d != 'start' and  d !='stop' and d !='quit' :
     print ("i dont understand ")
    elif d == 'help':
     print (help_text) 
    elif d == 'start':
     print(start)
    elif d == 'stop':
     print(stop) 
    elif d == "quit":
     print(quit_text)
     break #Exit the loop when 'quit' is entered


  

