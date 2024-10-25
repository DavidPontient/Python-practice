num=[1,2,5,4,5,6]
output= 11
def twosum(num, output):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j] == output:
               print("[{}, {}]".format(i, j))
    return []#return nothing 
        

twosum(num, output)