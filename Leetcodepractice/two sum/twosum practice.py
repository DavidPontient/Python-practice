nums = [6, 2, 8, 4, 5, 7]
target = 11
num_to_index = {}
def twosum(nums,target):
    for i, n in enumerate(nums):
        diff= target - n
        if diff in num_to_index:
            return [num_to_index[diff],i] # return the key which is index of diff( which is 11-6 = 5 ) and the index of n which is i
        num_to_index[n] = i  # assign each number to there index and store them in the dictionary/hashmap
    return []

print(twosum(nums, target))