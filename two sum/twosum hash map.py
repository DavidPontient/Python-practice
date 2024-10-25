nums = [2, 7, 11, 15]
target = 9
def two_sum(nums, target):
    # Create a dictionary to store the numbers we have seen so far and their indices
    num_to_index = {}

    # Loop through each number in the list
    for i, num in enumerate(nums):
        # Calculate the complement (number needed to reach the target)
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the complement and the current number
            return [num_to_index[complement], i]

        # Store the current number and its index in the dictionary
        num_to_index[num] = i

    # If no solution found, return an empty list (not expected in this problem)
    return []
print(two_sum(nums, target))


"""
# For the input nums = [2, 7, 11, 15] and target = 9:

# At i = 0, num = 2:

# Complement = 9 - 2 = 7.(target-num)
# 7 is not in the hash map, so we add 2: 0 to the hash map.
# At i = 1, num = 7:

# Complement = 9 - 7 = 2.
# 2 is in the hash map (from the previous step), so we return [0, 1].
"""

