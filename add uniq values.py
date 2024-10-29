def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates, then sum the elements of the set
    return sum(set(my_list))
#A set automatically removes duplicate elements, so only unique elements remain.