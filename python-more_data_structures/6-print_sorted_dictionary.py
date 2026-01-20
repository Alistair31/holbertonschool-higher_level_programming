#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortd = sorted(a_dictionary)
    for i in sortd:
        val = a_dictionary.get(i)
        print("{0}: {1}".format(i, val))
