#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replacedlist = []
    for i in range(0, len(my_list), 1):
        if my_list[i] == search:
            replacedlist.append(replace)
        else:
            replacedlist.append(my_list[i])
    return replacedlist
