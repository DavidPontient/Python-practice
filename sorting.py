l = [5,4,3,6,2,1]
# Using Bubble Sort to fully sort the list
while True:
    swapped = False
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            # Swap the elements
            l[i], l[i + 1] = l[i + 1], l[i]
            swapped = True
    # If no swaps happened, the list is sorted
    if not swapped:
        break
print(l)

