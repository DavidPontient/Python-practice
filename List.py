lsit=[]
my_list=[1,2,3,4,5] # count sstarts from 0 
# print(my_list[0])#outputs 1
my_list.append(6)
#print(my_list)#outputs [1,2,3,4,5,6]
my_list.insert(3, 'hello')
#print(my_list)#outputs [1,2,3,'hello',4,5,6]
my_list.remove(3)
#print(my_list)#outputs [1,2,'hello,4,5,6]
#print(my_list[1:4])#outputs [2,'hello',4]
#print(len(my_list))#basically the length outputs 6
reversed_list = my_list[::-1] # reverse list or use my_list.reverse()
for item in my_list:
    print(item) #can use this to view them in a straight list
for item in my_list:
    list.append(item)
