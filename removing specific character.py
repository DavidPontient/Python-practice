#!/usr/bin/python3
def no_c(my_string):
    return my_string.replace("C","").replace("c","")
#or
def no_c(my_string):
    my_string = my_string.translate({ord("c"): None})
    my_string = my_string.translate({ord("C"): None})
    return my_string