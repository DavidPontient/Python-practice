def duplicat(l: list[int]) -> int:
    j = 1  # Initialize j to point to the position of the next unique element
    for i in range(1, len(l)):  # Start iterating from the second element
        if l[i] != l[i - 1]:  # Compare current element with the previous one
            l[j] = l[i]  # Place the unique element at index j
            j += 1  # Increment j to point to the next position for unique elements
    return j  # j is the count of unique elements

     


