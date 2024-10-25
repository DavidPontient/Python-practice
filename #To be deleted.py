l = [5, 1, 1, 1, 5]
for i in l:
    if i == 5:
        print(i * "*")  # Prints 5 asterisks
    else:
        print("*   *")  # Prints asterisks with 3 spaces in between

# # Size of the heart
# for row in range(6):
#     for col in range(7):
#         if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  # Newline after each row


