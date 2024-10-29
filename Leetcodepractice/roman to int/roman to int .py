def lettertoint(s: str) -> int:
    lookup = { 
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    
    # reverse iteration solution, check the number from reverse
    output = 0
    last = "I"
    # Loop through the characters of string `s` from right to left
    #Check if the Current Character is Smaller than the Previous One:
    for char in s[::-1]:
        if lookup[char] < lookup[last]:
            output -= lookup[char]
        else:
            output += lookup[char]

        last=char  #update last to be the current character’s value for the next iteration.
    
    return output 

print(lettertoint("VX"))