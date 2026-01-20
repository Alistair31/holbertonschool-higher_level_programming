#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    sortlist = sorted(my_list, reverse=True)
    return sortlist[-1]
