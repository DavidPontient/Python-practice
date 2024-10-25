"""
for i in range(65,90):
    print(chr(i), end=" ") #chr turns numbers to there positional values in this case uppercase alphabet
"""
str="Pontient"
for i in str:
    if 97<= ord(i) <=122:
        i=chr(ord(i)-32)# ord turns characters to the positional number, its like the oposite of chr 
    print(i,end="")