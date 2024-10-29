l = [9, 4, 3, 5, 23]
largest = l[0] #we assume that the first number is the largest

for i in range(len(l)):
    if l[i] > largest:
        largest= l[i]
print(largest)
 