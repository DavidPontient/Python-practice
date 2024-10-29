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
    
    # Initialize output to 0
    output = 0
    
    # Loop through the characters of string `s` from left to right
    for char in s:
        if char in lookup:  # Check if the character exists in the lookup dictionary
            output += lookup[char]  # Add the corresponding value to the output
    
    return output

print(lettertoint("IV"))
