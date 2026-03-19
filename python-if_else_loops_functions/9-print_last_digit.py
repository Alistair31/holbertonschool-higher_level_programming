#!/usr/bin/python3
def print_last_digit(number):
    retlast = ""
    while str(number) != "":
        last = str(number)[-1:]
        retlast = retlast + str(last)
        return retlast
