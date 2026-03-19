#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checkedlist = []
    for i in range(0, len(my_list), 1):
        checkedlist.append(i % 2 == 0)
    return checkedlist
