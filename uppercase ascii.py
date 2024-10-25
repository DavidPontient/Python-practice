str="helloworld"
for char in str:
    if 'a' <= char <= 'z':
            # Convert lowercase character to uppercase by subtracting 32 from its ASCII value
        char=chr(ord(char) - 32)
    print("{}".format(char), end="")
print() 