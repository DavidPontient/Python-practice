def multiply_by_2(a_dictionary):
    # Create a new dictionary with keys and values multiplied by 2
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict
#OR
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for key, value in new_dict.items():
        new_dict[key] = value * 2
    return new_dict