def remove_char(string, index):
    if index < 0 or index >= len(string):
        return string
    return string[:index] + string[index+1:]
print(remove_char("Hello",4))